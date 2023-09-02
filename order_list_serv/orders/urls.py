from django.urls import path
from .views import OrderList, OrderDetail,OrderCreate


app_name = "orders"

urlpatterns = [
     path('all_orders/', OrderList.as_view()),  #get all orders
     path('order_detail/<int:pk>/', OrderDetail.as_view()), #get order detail all items
     path('order_create/', OrderCreate.as_view()) #create order with items (products

]
