import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from plates.models import Owner, NumberPlate
from plates.api import OwnerSerializer, NumberPlateSerializer


def index(request):
    owners = OwnerSerializer(Owner.objects.all(), many=True)
    number_plates = NumberPlateSerializer(NumberPlate.objects.all(), many=True)
    initial_data = json.dumps({
        'owners': owners.data,
        'number_plates': number_plates.data,
    }, cls=DjangoJSONEncoder)
    return render(request, 'index.html', {
        'initial_data': initial_data
    })
