import pytest
from django.urls import reverse

from tests.factories import ProductFactory


@pytest.mark.django_db
def test_product_delete(auth_client):
    products = ProductFactory.create_batch(5)

    response = auth_client.delete(
        path=reverse('network:product_view', args=[products[0].id]),
    )

    assert response.status_code == 204
