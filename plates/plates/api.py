import re

from rest_framework import serializers, viewsets
from rest_framework import filters
from rest_framework.views import exception_handler
from rest_framework.validators import UniqueTogetherValidator

from plates.models import Owner, NumberPlate



class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    number_plate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Owner.objects.all(),
                fields=('first_name', 'last_name'),
                message='Owner already exists with this first and last names'
            )
        ]


class NumberPlateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)

    class Meta:
        model = NumberPlate
        fields = '__all__'

    def validate_number(self, value):
        # There are a lot of different formats of plate numbers, see:
        # https://regitra.lt/lt/paslaugos-ir-veikla/numerio-zenklai/numerio-zenklu-tipai
        # So a general rule for lithuanian number plate format is applied
        only_letters_and_numbers = re.compile("^[a-zA-Z0-9]*$")

        if not only_letters_and_numbers.match(value):
            raise serializers.ValidationError("Only english letters and numbers "
                                              "are allowed in car number plates")
        return value



class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class NumberPlateViewSet(viewsets.ModelViewSet):
    queryset = NumberPlate.objects.all()
    serializer_class = NumberPlateSerializer
