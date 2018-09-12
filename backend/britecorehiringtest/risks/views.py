from rest_framework import viewsets

from .models import RiskType, Field, FieldType
from .serializers import RiskTypeSerializer, FieldSerializer, FieldTypeSerializer


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    RiskType API view set.
    """
    queryset = RiskType.objects.all().prefetch_related('fields', 'fields__options', 'fields__field_type')
    serializer_class = RiskTypeSerializer


class FieldViewSet(viewsets.ModelViewSet):
    """
    Field API view set.
    """
    queryset = Field.objects.all().select_related('field_type').prefetch_related('options')
    serializer_class = FieldSerializer


class FieldTypeViewSet(viewsets.ModelViewSet):
    """
    Field Type API view set.
    """
    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
