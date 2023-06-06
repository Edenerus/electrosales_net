import pytest
from django.urls import reverse

from network.serializers import ProviderSerializer
from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_provider_detail(auth_client):
    provider = ProviderFactory.create()

    response = auth_client.get(
        path=reverse('network:provider_view', args=[provider.id], ),
    )
    print(response.data)
    print(ProviderSerializer(provider).data)
    assert response.status_code == 200
    assert response.data == ProviderSerializer(provider).data
