from django.contrib import admin

from risks.models import RiskType, Field, FieldType, RiskEntry, RiskEntryValues, EnumOption


admin.site.register(RiskType)
admin.site.register(Field)
admin.site.register(FieldType)
admin.site.register(RiskEntry)
admin.site.register(RiskEntryValues)
admin.site.register(EnumOption)