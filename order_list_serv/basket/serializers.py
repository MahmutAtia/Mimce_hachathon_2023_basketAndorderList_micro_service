# basket/serializers.py

from rest_framework import serializers
from .models import BasketItem


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'

# class BasketSerializer(serializers.ModelSerializer):
#     basket_items = BasketItemSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = theCustomer
#         fields = '__all__'
