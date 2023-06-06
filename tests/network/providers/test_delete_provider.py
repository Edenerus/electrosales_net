import pytest
from django.urls import reverse

from tests.factories import ProviderFactory


@pytest.mark.django_db
def test_provider_delete(auth_client):
    provider = ProviderFactory.create()

    response = auth_client.delete(
        path=reverse('network:provider_view', args=[provider.id]),
    )

    assert response.status_code == 204
