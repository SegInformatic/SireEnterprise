from rest_framework import serializers
from django.contrib.auth.models import User

from gob.models import Empresa


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class EmpresaSerializer(serializers.ModelSerializer):
    razon_social_display_webix = serializers.CharField(source='razon_social', read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = '__all__'
