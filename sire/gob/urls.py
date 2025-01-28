from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gob.views import (
    EmpresaViewSet,
    ClienteViewSet,
    FacturaElectronicaViewSet,
    logout_view,
    login_view,
    aviso_privacidad_view,
    custom_login,
)


router = DefaultRouter()
router.register(r'empresa', EmpresaViewSet, basename='empresa')
router.register(r'cliente', ClienteViewSet, basename='cliente')
router.register(r'factura', FacturaElectronicaViewSet, basename='factura')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('aviso-privacidad/', aviso_privacidad_view, name='aviso_privacidad'),
    path('api-login/', custom_login, name='api_login'),
]
