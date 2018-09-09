""" Serializers for Risks app. """
from rest_framework import serializers

from .models import RiskType, Field, FieldType


class FieldTypeSerializer(serializers.ModelSerializer):
    """
    FieldType Model serializer.
    """
    class Meta:
        model = FieldType
        fields = ('id', 'name',)


class FieldSerializer(serializers.ModelSerializer):
    """
    Field Model serializer.
    """
    field_type = serializers.SlugRelatedField(
        queryset=FieldType.objects.all(),
        slug_field='name',
    )
    options = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='value',
    )

    class Meta:
        model = Field
        fields = ('risk_type', 'field_type', 'name', 'options')
        extra_kwargs = {'risk_type': {'write_only': True}}


class RiskTypeSerializer(serializers.ModelSerializer):
    """
    Risk Type Model serializer.
    """
    fields = FieldSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'fields')
