from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from gob.models import (
    Empresa,
    Cliente,
    FacturaElectronica,
    Right,
    GroupRight,
)

models = [
    Empresa,
    Cliente,
    FacturaElectronica,
    Right,
    GroupRight,
]

for model in models:
    admin.site.register(model, ImportExportModelAdmin)
