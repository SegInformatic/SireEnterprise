from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from gob.models import Cliente

class FacturaElectronica(models.Model):
    ACTIVA = 1
    PAGADA = 2
    CANCELADA = 3
    ESTATUS = (
        (ACTIVA, 'Activa'),
        (PAGADA, 'Pagada'),
        (CANCELADA, 'Cancelada'),
    )

    MXP = 1
    USD = 2
    MONEDA = (
        (MXP, 'Pesos Mexicanos'),
        (USD, 'Dólares Americanos'),
    )

    NORMAL = 1
    ANTICIPO = 2
    NOTA_CREDITO = 3
    NOTA_CARGO = 4
    EFECTO_CONTABLE = (
        (NORMAL, 'Normal'),
        (ANTICIPO, 'Anticipo'),
        (NOTA_CREDITO, 'Nota de Credito'),
        (NOTA_CARGO, 'Nota Cargo'),
    )

    estatus = models.SmallIntegerField(choices=ESTATUS, verbose_name=_('Estatus'), default=ACTIVA)
    cliente = models.ForeignKey(Cliente, related_name='facturas', on_delete=models.CASCADE, blank=False, null=False, default=1)
    subtotal = models.DecimalField(max_digits=16, decimal_places=4, default=0, blank=False, null=False)
    total = models.DecimalField(max_digits=16, decimal_places=4, default=0, blank=False, null=False)
    folio_timbrado = models.IntegerField(verbose_name='Folio de timbrado', unique=True, blank=True, default=1)
    moneda = models.SmallIntegerField(choices=MONEDA, default=MXP)
    fecha_emision = models.DateField(default=timezone.now)
    efecto_contable = models.SmallIntegerField(choices=EFECTO_CONTABLE, verbose_name=_('Efecto contable'), default=NORMAL)
