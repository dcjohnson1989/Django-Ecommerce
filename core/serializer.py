from rest_framework import serializers
from .models import Item, OrderItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'price', 'discount_price', 'category', 'label', 'slug', 'stock_no',
                  'description_short', 'description_long', 'image', 'is_active')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('user', 'item', 'quantity')



