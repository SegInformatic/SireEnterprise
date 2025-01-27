from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gob.views import (
    EmpresaViewSet,
    ClienteViewSet,
    FacturaElectronicaViewSet
)


router = DefaultRouter()
router.register(r'empresa', EmpresaViewSet, basename='empresa')
router.register(r'cliente', ClienteViewSet, basename='cliente')
router.register(r'factura', FacturaElectronicaViewSet, basename='factura')

urlpatterns = [
    path('', include(router.urls)),
]
