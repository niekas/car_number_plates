from django.shortcuts import render

from plates.models import Owner, NumberPlate


def index(request):
    return render(request, 'index.html', {
        'owners' : Owner.objects.all(),
        'number_plates': NumberPlate.objects.all()
    })
