from rest_framework import serializers

from network.models import Provider, Product


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'title', 'country', 'supplier', 'debt', 'product')
        read_only_fields = ('debt', 'level', )

    """read_only т.к запрещаем редактировать задолженность"""
    product = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
