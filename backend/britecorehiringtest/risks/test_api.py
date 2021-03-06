""" Tests for Risks app API """
import json

import pytest

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APIClient

from .views import RiskTypeViewSet


@pytest.mark.django_db
class TestRisksAPI():
    """ Test cases for Risks API """

    def setup_method(self):
        """
        Setup tests.
        """
        self.factory = APIRequestFactory()
        self.view = RiskTypeViewSet.as_view({'get': 'list'})
        self.viewDetail = RiskTypeViewSet.as_view({'get': 'retrieve'})
        self.client = APIClient()

    def test_empty_risk_type_request(self):
        """
        Test getting empty list of risk_types
        """
        request = self.factory.get('/risk_type/', format='json')
        response = self.view(request)
        response.render()
        assert json.loads(response.content) == []
        assert response.status_code == 200

    def test_risk_type_add(self):
        """
        Tests adding a new risk_type.
        """
        self.client.post(reverse('risks:risktype-list'), {'name': 'Automobile'}, format='json')
        self.client.post(reverse('risks:fieldtype-list'), {'name': 'text'}, format='json')
        self.client.post(
            reverse('risks:field-list'),
            {
                'name': 'brand',
                'risk_type': 1,
                'field_type': 'text',
            },
            format='json'
        )
        request = self.factory.get(reverse('risks:risktype-list'), format='json')
        response = self.view(request)
        response.render()
        assert json.loads(response.content) == [
            {
                'fields': [
                    {
                        'field_type': 'text',
                        'name': 'brand',
                        'options': [],
                    }
                ],
                'id': 1,
                'name': 'Automobile',
            }
        ]
        assert response.status_code == 200

    def test_risk_type_get(self):
        """
        Test get one risk type by pk
        """
        self.client.post(reverse('risks:risktype-list'), {'name': 'Automobile'}, format='json')
        request = self.factory.get(reverse('risks:risktype-detail', kwargs={'pk': 2}), format='json')
        response = self.viewDetail(request, pk='2')
        response.render()
        assert json.loads(response.content) == {
            'fields': [],
            'id': 2,
            'name': 'Automobile'
        }
