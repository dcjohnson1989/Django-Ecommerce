from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    OrderHistoryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    ItemList,
    ItemDetail,
    OrderItemList,
    OrderCart
)

app_name = 'core'

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('api/items', ItemList.as_view(), name='item_api'),
    path('api/item/<slug>', ItemDetail.as_view(), name='item_detail_api'),
    path('api/cart_items', OrderItemList.as_view(), name='cart_item_list'),
    path('api/order_cart', OrderCart.as_view(), name='order_cart_api'),
    url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger')
]
