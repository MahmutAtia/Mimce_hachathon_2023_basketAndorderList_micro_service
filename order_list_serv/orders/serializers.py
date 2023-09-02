from rest_framework import serializers
from .models import Order, Product
from .utlis import get_product_id_list


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'product_price', 'product_description', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    item = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('order_id', 'user_id', 'order_date', 'adress' ,"item" )

class OrderCreateSerializer(serializers.ModelSerializer):
    item = ProductSerializer(many=True, write_only=True)
    class Meta:
        model = Order
        fields = ( "user_id", "adress", "item")

    def create(self, validated_data):
        items_data = validated_data.pop('item')

        print(validated_data)
        order = Order.objects.create(**validated_data)
        product_id_list = get_product_id_list(items_data)
        print(product_id_list)

        
        for item in items_data:

            Product.objects.create(order=order, **item)
        return order