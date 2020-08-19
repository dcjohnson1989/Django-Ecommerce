from rest_framework import serializers
from .models import Item, OrderItem, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'price', 'discount_price', 'category', 'label', 'slug', 'stock_no',
                  'description_short', 'description_long', 'image', 'is_active')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'user', 'item', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'ref_code', 'items', 'start_date', 'ordered_date', 'ordered', 'shipping_address',
                  'billing_address', 'payment', 'coupon', 'being_delivered', 'received', 'refund_requested',
                  'refund_granted')

