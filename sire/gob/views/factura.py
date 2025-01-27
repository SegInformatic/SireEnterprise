from rest_framework.viewsets import ModelViewSet

from gob.models import FacturaElectronica
from gob.serializers import FacturaSerializer


class FacturaElectronicaViewSet(ModelViewSet):
    model = FacturaElectronica
    serializer_class = FacturaSerializer

    def get_queryset(self):
        user = self.request.user
        empresas = user.empresas.all()
        queryset = FacturaElectronica.objects.filter(cliente__empresa__in=empresas)

        empresa_id = self.request.query_params.get('empresa', None)

        if empresa_id:
            queryset = queryset.filter(cliente__empresa_id=empresa_id)

        return queryset

    def perform_create(self, serializer):
        cliente = serializer.validated_data.get('cliente')
        empresa = cliente.empresa
        instance = serializer.save()
        instance.empresa = empresa
        instance.save()

    def perform_update(self, serializer):
        cliente = serializer.validated_data.get('cliente')
        empresa = cliente.empresa
        instance = serializer.save()
        instance.empresa = empresa
        instance.save()
