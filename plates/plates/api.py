import re

from rest_framework import serializers, viewsets
from rest_framework import filters

from plates.models import Owner, NumberPlate

only_letters_and_numbers = re.compile("^[a-zA-Z0-9]*$")



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

    def validate(self, data):
        if not only_letters_and_numbers.match(data['number']):
            raise serializers.ValidationError("Only english letters and numbers "
                                              "are allowed in car number plates")
        return data



class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class NumberPlateViewSet(viewsets.ModelViewSet):
    queryset = NumberPlate.objects.all()
    serializer_class = NumberPlateSerializer
