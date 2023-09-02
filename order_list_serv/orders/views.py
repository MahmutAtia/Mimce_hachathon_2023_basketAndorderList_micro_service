from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer, OrderCreateSerializer


# Create your views here.

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        return Product.objects.filter(order_id=order_id)
    


class OrderCreate(CreateAPIView):
    serializer_class = OrderCreateSerializer
   
   

