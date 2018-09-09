from django.contrib import admin

from .models import RiskType, Field, FieldType, RiskEntry, RiskEntryValues, EnumOption


admin.site.register(RiskType)
admin.site.register(Field)
admin.site.register(FieldType)
admin.site.register(RiskEntry)
admin.site.register(RiskEntryValues)
admin.site.register(EnumOption)
