from rest_framework import serializers
from .models import ShopUser

class ShopUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['id', 'url', 'username', 'email']
