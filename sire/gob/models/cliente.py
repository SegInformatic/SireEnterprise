from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
import re

from gob.models import Empresa


class Cliente(models.Model):

    def validar_rfc(value):
        """
        Valida el formato del RFC (persona física o moral).
        """
        rfc_pattern = re.compile(
            r'^([A-ZÑ&]{3,4})'  # Letras iniciales (3 para moral, 4 para físicas)
            r'(\d{2})(\d{2})(\d{2})'  # Fecha en formato AA/MM/DD
            r'([A-Z\d]{3})$'  # Homoclave alfanumérica
        )

        if not rfc_pattern.match(value):
            raise ValidationError('El RFC no tiene un formato válido.')

        return value

    razon_social = models.CharField(max_length=255)
    rfc = models.CharField(
        max_length=13,
        unique=True,
        null=False,
        blank=False,
        validators=[validar_rfc]
        )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes', null=True, blank=True)
    direccion_fiscal = models.TextField(
        validators=[MinLengthValidator(10, message="La dirección fiscal debe tener al menos 10 caracteres")]
        )
    contacto_principal = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    telefono_contacto = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Debe ser un número de 10 dígitos.")],
        help_text="Teléfono de la persona de contacto."
    )
    forma_pago = models.CharField(max_length=100)
    cuenta_pago = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^\d{10,18}$',
                message="La cuenta de pago debe tener entre 10 y 18 dígitos."
            )
            ]
        )
