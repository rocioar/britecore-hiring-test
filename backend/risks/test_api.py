""" Tests for Risks app API """
import json

import pytest

from django.urls import reverse

from rest_framework.test import APIRequestFactory, APIClient

from risks.views import RiskTypeViewSet


@pytest.mark.django_db
class TestRisksAPI():
    """ Test cases for Risks API """

    def setup_method(self):
        """
        Setup tests.
        """
        self.factory = APIRequestFactory()
        self.view = RiskTypeViewSet.as_view({'get': 'list'})
        self.client = APIClient()

    def test_empty_risk_type_request(self):
        """ Test getting empty list of risk_types """
        request = self.factory.get('/risk_type/', format='json')
        response = self.view(request)
        response.render()
        assert json.loads(response.content) == []
        assert response.status_code == 200

    def test_risk_type_add(self):
        """
        Tests adding a new risk_type.
        """
        self.client.post('/risk_type/', {'name': 'Automobile'}, format='json')
        self.client.post('/field_type/', {'name': 'text'}, format='json')
        self.client.post(
            '/field/',
            {
                'name': 'brand',
                'risk_type': 1,
                'field_type': 'text',
            },
            format='json'
        )
        request = self.factory.get('/risk_type/', format='json')
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