from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Modelo personalizado de usuario que extiende el modelo predeterminado de Django."""
    email = models.EmailField(unique=True)  # Hacer que el correo sea único
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Campo opcional
    address = models.TextField(blank=True, null=True)  # Dirección opcional
    is_active = models.BooleanField(default=True)  # Usuario activo o inactivo

    def __str__(self):
        return self.username