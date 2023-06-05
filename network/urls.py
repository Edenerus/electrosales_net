from django.urls import path

from network.views import provider, product

urlpatterns = [
    path('product/list', product.ProductListView.as_view(), name='product_list'),
    path('product/create', product.ProductCreateView.as_view(), name='product_create_view'),
    path('product/<pk>', product.ProductView.as_view(), name='product_view'),

    path('provider/list', provider.ProviderListView.as_view(), name='provider_list'),
    path('provider/create', provider.ProviderCreateView.as_view(), name='provider_create_view'),
    path('provider/<pk>', provider.ProviderView.as_view(), name='provider_view'),

]
