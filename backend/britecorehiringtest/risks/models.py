"""
Risk Types models definition
"""
from model_utils.models import TimeStampedModel
from model_utils import Choices

from django.db import models


class FieldType(models.Model):
    """
    Represent a field type.
    """
    FIELD_TYPE = Choices('text', 'number', 'date', 'enum')
    name = models.CharField(max_length=255, choices=FIELD_TYPE)

    class Meta:
        verbose_name = 'Field Type'
        verbose_name_plural = 'Field Types'

    def __str__(self):
        return self.name


class RiskType(models.Model):
    """
    Represents a risk type.
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Risk Type'
        verbose_name_plural = 'Risk Types'

    def __str__(self):
        return self.name


class Field(models.Model):
    """
    Represents a generic field belonging to a risk type.
    """
    risk_type = models.ForeignKey(RiskType, related_name="fields", on_delete=models.CASCADE)
    field_type = models.ForeignKey(FieldType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'

    def __str__(self):
        return self.name


class EnumOption(models.Model):
    """
    Represents an option belonging to a field of the type enum.
    """
    value = models.CharField(max_length=255)
    field = models.ForeignKey(Field, related_name='options', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Enum Option'
        verbose_name_plural = 'Enum Options'

    def __str__(self):
        return self.value


class RiskEntry(TimeStampedModel):
    """
    Represents a risk entry.
    """
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Risk Entry'
        verbose_name_plural = 'Risk Entries'

    def __str__(self):
        return self.risk_type


class RiskEntryValues(models.Model):
    """
    Represent the Risks Entry field values.
    """
    risk_entry = models.ForeignKey(RiskEntry, related_name='values', on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Risk Entry Value'
        verbose_name_plural = 'Risk Entry Values'

    def __str__(self):
        return f"{self.risk_entry}: {self.value}"
