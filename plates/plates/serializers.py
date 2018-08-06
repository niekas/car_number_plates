import re

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Owner, NumberPlate


class OwnerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    number_plate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Owner.objects.all(),
                fields=('first_name', 'last_name'),
                message='Owner already exists with such first and last names'
            )
        ]


class NumberPlateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    owner_full_name = serializers.StringRelatedField(source='owner')

    class Meta:
        model = NumberPlate
        fields = '__all__'

    def validate_number(self, value):
        # https://regitra.lt/lt/paslaugos-ir-veikla/numerio-zenklai/numerio-zenklu-tipai
        lt_number_plate_format = re.compile("^[a-zA-Z0-9]{1,6}$")

        if not lt_number_plate_format.match(value):
            raise serializers.ValidationError("Up to 6 english letters and "
                       "numbers are allowed in lithuanian car number plates")
        return value
