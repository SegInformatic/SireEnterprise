from rest_framework import serializers

from gob.models import FacturaElectronica


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaElectronica
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('empresa', None)
        return super().create(validated_data)
