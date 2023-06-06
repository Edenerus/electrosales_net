import pytest
from django.urls import reverse

from tests.factories import ProductFactory


@pytest.mark.django_db
def test_products_list(auth_client):
    products = ProductFactory.create_batch(10)

    response = auth_client.get(
        path=reverse('network:product_list'),
    )

    assert response.status_code == 200
    assert len(response.data['results']) == 10
