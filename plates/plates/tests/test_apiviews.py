import json

from rest_framework import status

from django.db.utils import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

from plates.apiviews import OwnerViewSet, NumberPlateViewSet
from plates.models import Owner, NumberPlate


class TestOwnerAPI(TestCase):
    def setUp(self):
        self.client = Client()
        Owner.objects.create(first_name='John', last_name='Brown')
        Owner.objects.create(first_name='Tom', last_name='Gray')

    def test_owner_detail(self):
        owner = Owner.objects.get(pk=1)
        url = reverse('owner-detail', kwargs={'pk': owner.pk})
        self.assertEqual(url, '/api/owners/1/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Brown',
            'number_plate': []
        })

    def test_owner_list(self):
        url = reverse('owner-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            'id': 1,
            'first_name': 'John',
            'last_name': 'Brown',
            'number_plate': []
         }, {
            'id': 2,
            'first_name': 'Tom',
            'last_name': 'Gray',
            'number_plate': [],
        }])

    def test_owner_create(self):
        url = reverse('owner-list')
        response = self.client.post(url, {
            'first_name': 'Bob',
            'last_name': 'Smith'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        owner = Owner.objects.last()
        self.assertEqual(owner.first_name, 'Bob')
        self.assertEqual(owner.last_name, 'Smith')

    def test_owner_update(self):
        url = reverse('owner-detail', kwargs={'pk': 2})
        response = self.client.patch(url, json.dumps({
            'last_name': 'White'
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        owner = Owner.objects.get(pk=2)
        self.assertEqual(owner.first_name, 'Tom')
        self.assertEqual(owner.last_name, 'White')
        response = self.client.patch(url, json.dumps({
            'first_name': 'Robin'
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        owner = Owner.objects.get(pk=2)
        self.assertEqual(owner.first_name, 'Robin')
        self.assertEqual(owner.last_name, 'White')

    def test_owner_delete(self):
        url = reverse('owner-detail', kwargs={'pk': 1})
        response = self.client.delete(url, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Owner.objects.count(), 1)


class TestNumberPlateAPI(TestCase):
    def setUp(self):
        self.client = Client()
        owner1 = Owner.objects.create(first_name='John', last_name='Brown')
        owner2 = Owner.objects.create(first_name='Tom', last_name='Gray')
        NumberPlate.objects.create(number='ABC123', owner=owner1)
        NumberPlate.objects.create(number='EVO789', owner=owner1)
        NumberPlate.objects.create(number='CPP536', owner=owner2)
        NumberPlate.objects.create(number='VLN989', owner=owner2)

    def test_number_plate_detail(self):
        number_plate = NumberPlate.objects.get(pk=1)
        url = reverse('numberplate-detail', kwargs={'pk': number_plate.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'number': number_plate.number,
            'owner_id': number_plate.owner.pk,
            'owner_full_name': str(number_plate.owner)
        })

    def test_number_plate_list(self):
        url = reverse('numberplate-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            'id': 1,
            'number': 'ABC123',
            'owner_id': 1,
            'owner_full_name': 'John Brown'
         }, {
            'id': 2,
            'number': 'EVO789',
            'owner_id': 1,
            'owner_full_name': 'John Brown'
         }, {
            'id': 3,
            'number': 'CPP536',
            'owner_id': 2,
            'owner_full_name': 'Tom Gray'
         }, {
            'id': 4,
            'number': 'VLN989',
            'owner_id': 2,
            'owner_full_name': 'Tom Gray'
        }])

    def test_number_plate_create(self):
        url = reverse('numberplate-list')
        response = self.client.post(url, {
            'number': 'aaa111',
            'owner_id': 1
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        number_plate = NumberPlate.objects.last()
        self.assertEqual(number_plate.number, 'AAA111')
        self.assertEqual(number_plate.owner.pk, 1)

    def test_number_plate_update(self):
        url = reverse('numberplate-detail', kwargs={'pk': 1})
        response = self.client.patch(url, json.dumps({
            'number': 'abc111'
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        number_plate = NumberPlate.objects.get(pk=1)
        self.assertEqual(number_plate.number, 'ABC111')
        self.assertEqual(number_plate.owner.pk, 1)
        response = self.client.patch(url, json.dumps({
            'owner_id': 2
        }), content_type='application/json')
        number_plate = NumberPlate.objects.get(pk=1)
        self.assertEqual(number_plate.number, 'ABC111')
        self.assertEqual(number_plate.owner.pk, 2)
        with self.assertRaises(IntegrityError):
            response = self.client.patch(url, json.dumps({
                'owner_id': 2,
                'number': 'evo789'
            }), content_type='application/json')

    def test_number_plate_delete(self):
        url = reverse('numberplate-detail', kwargs={'pk': 1})
        response = self.client.delete(url, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(NumberPlate.objects.count(), 3)

    def test_owner_delete(self):
        url = reverse('owner-detail', kwargs={'pk': 1})
        response = self.client.delete(url, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(NumberPlate.objects.count(), 2)
