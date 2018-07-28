from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from plates import api
from plates import views


router = DefaultRouter()
router.register('owners', api.OwnerViewSet)
router.register('numberplates', api.NumberPlateViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
