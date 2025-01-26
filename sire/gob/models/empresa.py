from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import re


class Empresa(models.Model):
    REGIMEN_FISCAL_CHOICES = (
        ('GENERAL', 'General de Ley'),
        ('SIMPLIFICADO', 'Régimen Simplificado de Confianza'),
        ('RESIDENTE', 'Residente en el Extranjero'),
    )

    def validar_rfc(value):
        """
        Valida el formato del RFC (persona física o moral).
        """
        rfc_pattern = re.compile(
            r'^([A-ZÑ&]{3,4})'
            r'(\d{2})(\d{2})(\d{2})'  # Fecha en formato AA/MM/DD
            r'([A-Z\d]{3})$'  # Homoclave alfanumérica
        )

        if not rfc_pattern.match(value):
            raise ValidationError('El RFC no tiene un formato válido.')

        return value

    rfc = models.CharField(max_length=13, unique=True, validators=[validar_rfc])
    regimen_fiscal = models.CharField(max_length=12, choices=REGIMEN_FISCAL_CHOICES)
    nombre_contacto = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre de contacto solo puede contener letras y espacios."
                )
                ],
        help_text="Nombre de la persona de contacto."
        )
    telefono_contacto = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Debe ser un número de 10 dígitos.")],
        help_text="Teléfono de la persona de contacto."
    )

    razon_social = models.CharField(
        max_length=255, blank=False,
        validators=[MinLengthValidator(5)],
        help_text="Nombre de la empresa o persona física."
        )
    direccion_fiscal = models.TextField(
        blank=False,
        validators=[MinLengthValidator(5)],
        help_text="Dirección fiscal de la empresa o persona física."
        )
    codigo_postal = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{5}$')])
    users = models.ManyToManyField(User, related_name='empresas')
    certificado = models.FileField(
        upload_to='empresas/cer/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['cer'])]
    )
    cer_key = models.FileField(
        upload_to='empresas/key/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['key'])]
    )

    def __str__(self):
        return f'{self.razon_social} ({self.rfc})'
