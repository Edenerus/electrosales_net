import pytest
from django.urls import reverse

from network.serializers import ProductSerializer
from tests.factories import ProductFactory


@pytest.mark.django_db
def test_product_detail(auth_client):

    products = ProductFactory.create_batch(5)

    response = auth_client.get(
        path=reverse('network:product_view', args=[products[0].id]),
    )

    assert response.status_code == 200
    assert response.data == ProductSerializer(products[0]).data
