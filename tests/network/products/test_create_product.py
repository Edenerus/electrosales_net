import pytest
from django.urls import reverse
from rest_framework import status

from network.models import Product


@pytest.mark.django_db
class TestProductCreate:
    url = reverse('network:product_create_view')

    def test_create_successful(self, auth_client):
        response = auth_client.post(self.url, data={
            "title": "test_product",
            "model": "model",
            })

        product = Product.objects.last()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': product.id,
            "date_release": product.date_release,
            "title": product.title,
            "model": product.model
        }

    def test_create_unauthorized(self, client):
        response = client.post(self.url, data={})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_invalid_data(self, auth_client):
        response = auth_client.post(self.url, data={
            'model': True,
            'title': int(5),
            'date_release': "data",
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not Product.objects.last()
