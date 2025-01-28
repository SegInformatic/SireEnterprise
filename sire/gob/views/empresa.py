from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from gob.models import Empresa
from gob.serializers.empresa import EmpresaSerializer
from gob.permissions import has_right_permission


class EmpresaViewSet(ModelViewSet):
    required_right = 'empresa'
    model = Empresa
    serializer_class = EmpresaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, has_right_permission(required_right)]

    def get_queryset(self):
        user = self.request.user
        return Empresa.objects.filter(users=user.id)
        
    def perform_create(self, serializer):
        empresa = serializer.save()
        empresa.users.add(self.request.user)

    def perform_update(self, serializer):
        empresa = serializer.save()
        if not empresa.users.filter(id=self.request.user.id).exists():
            raise PermissionDenied("No tienes permiso para editar esta empresa.")
