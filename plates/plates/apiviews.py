from rest_framework import viewsets

from .serializers import OwnerSerializer, NumberPlateSerializer
from .models import Owner, NumberPlate


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class NumberPlateViewSet(viewsets.ModelViewSet):
    queryset = NumberPlate.objects.all()
    serializer_class = NumberPlateSerializer
