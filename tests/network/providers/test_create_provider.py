import pytest
from django.urls import reverse
from rest_framework import status

from network.models import Provider


@pytest.mark.django_db
class TestProviderCreate:
    url = reverse('network:provider_create_view')

    def test_create_successful(self, auth_client):
        response = auth_client.post(self.url, data={
            "title": "test_title",
            "type": 'type',
            "email": "test@mail.ru",
            "country": "test",
            "city": "test",
            "street": "test",
            "house": "test"
            })

        provider = Provider.objects.last()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "id": provider.id,
            "title": provider.title,
            "country": provider.country,
            "debt": '0.00',
            "supplier": [],
            }

    def test_create_unauthorized(self, client):
        response = client.post(self.url, data={})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_invalid_data(self, auth_client):
        response = auth_client.post(self.url, data={
            "title": "test22_title",
            "type": 0,
            "email": "test22@mail.ru",
            "country": "test",
            "city": "test",
            "street": "test",
            "house": "test",
            "supplier": 'None',
            "debt": "0.00"
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not Provider.objects.last()
