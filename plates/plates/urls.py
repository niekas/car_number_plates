from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .apiviews import OwnerViewSet, NumberPlateViewSet
from .views import index


router = DefaultRouter()
router.register('owners', OwnerViewSet)
router.register('numberplates', NumberPlateViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
