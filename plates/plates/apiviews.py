from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from django.db.utils import IntegrityError

from .serializers import OwnerSerializer, NumberPlateSerializer
from .models import Owner, NumberPlate


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class NumberPlateViewSet(viewsets.ModelViewSet):
    queryset = NumberPlate.objects.all()
    serializer_class = NumberPlateSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super(NumberPlateViewSet, self).create(request, *args, **kwargs)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'number': ['This number plate already exists, please choose a different one.']
            })
