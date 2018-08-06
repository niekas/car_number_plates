from django.contrib import admin
from .models import NumberPlate, Owner


admin.register(Owner, NumberPlate)(admin.ModelAdmin)
