from rest_framework import serializers
from .models import Order, Product
from authentication.models import ShopUser

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.id')
    product = serializers.ReadOnlyField(source='product.id')
    class Meta:
        model = Order
        fields = ['buyer', 'product', 'quantyty']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.id')
    class Meta:
        model = Product
        fields = ['sellser', 'name', 'price_in_cents', 'quantity_in_stock'
                  ,'description']
