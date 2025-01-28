from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from gob.models import Cliente
from gob.serializers import ClienteSerializer
from gob.permissions import has_right_permission



class ClienteViewSet(ModelViewSet):
    required_right = 'cliente'
    model = Cliente
    serializer_class = ClienteSerializer
    authentication_classes = [TokenAuthentication, IsAuthenticated]
    permission_classes = [has_right_permission(required_right)]

    def get_queryset(self):
        user = self.request.user
        empresas = user.empresas.all()
        queryset = Cliente.objects.filter(empresa__in=empresas)
        
        empresa_id = self.request.query_params.get('empresa', None)

        if empresa_id:
            queryset = queryset.filter(empresa_id=empresa_id)

        return queryset
    
    def perform_create(self, serializer):
        empresa = serializer.validated_data.get('empresa', self.request.user.empresas.first())
        serializer.save(empresa=empresa)

    def perform_update(self, serializer):
        empresa = serializer.validated_data.get('empresa', self.request.user.empresas.first()) 
        serializer.save(empresa=empresa)
