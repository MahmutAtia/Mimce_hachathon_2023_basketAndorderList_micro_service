from rest_framework import serializers
from .models import Order, Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'user_id', 'order_date')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'product_price', 'product_description', 'quantity')


class OrderCreateSerializer(serializers.ModelSerializer):
    item = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ("order_id", "user_id", "adress", "item")

    def create(self, validated_data):
        items_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)

        
        for item in items_data:
            Product.objects.create(order=order, **item)
        return order