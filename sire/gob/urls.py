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
    deslinde_responsabilidad_view,  # Importamos la nueva vista
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
    path('deslinde/', deslinde_responsabilidad_view, name='deslinde'),  # Nueva URL
    path('api-login/', custom_login, name='api_login'),
]
