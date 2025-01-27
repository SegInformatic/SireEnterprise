from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from gob.models import Empresa
from gob.serializers.empresa import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    model = Empresa
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        user = self.request.user
        return Empresa.objects.filter(users=user)
        
    def perform_create(self, serializer):
        empresa = serializer.save()
        empresa.users.add(self.request.user)

    def perform_update(self, serializer):
        empresa = serializer.save()
        if not empresa.users.filter(id=self.request.user.id).exists():
            raise PermissionDenied("No tienes permiso para editar esta empresa.")
