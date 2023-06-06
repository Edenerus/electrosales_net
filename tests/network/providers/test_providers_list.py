import pytest
from django.urls import reverse

from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_providers_list(auth_client):
    providers = ProviderFactory.create_batch(10)

    response = auth_client.get(
        path=reverse('network:provider_list'),
    )

    assert response.status_code == 200
    assert len(response.data['results']) == 10
