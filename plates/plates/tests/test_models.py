from django.db.utils import IntegrityError
from django.test import TestCase

from plates.models import Owner, NumberPlate


class TestOwnerAPI(TestCase):
    def setUp(self):
        owner = Owner.objects.create(first_name='John', last_name='Brown')
        NumberPlate.objects.create(number='ABC123', owner=owner)
        NumberPlate.objects.create(number='EVO789', owner=owner)

    def test_owner_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            Owner.objects.create(first_name='John', last_name='Brown')

    def test_number_plate_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            NumberPlate.objects.create(number='EVO789', owner=Owner.objects.last())

    def test_number_plate_saved_as_upper_case(self):
        NumberPlate.objects.create(number='evo888', owner=Owner.objects.last())
        number_plate = NumberPlate.objects.last()
        self.assertEqual(number_plate.number, 'EVO888')
        number_plate.number = 'evo999'
        number_plate.save()
        self.assertEqual(number_plate.number, 'EVO999')
