from rest_framework import serializers, viewsets
from rest_framework import filters

from plates.models import Owner, NumberPlate


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    number_plate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = '__all__'


class NumberPlateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)

    class Meta:
        model = NumberPlate
        fields = '__all__'


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class NumberPlateViewSet(viewsets.ModelViewSet):
    queryset = NumberPlate.objects.all()
    serializer_class = NumberPlateSerializer
