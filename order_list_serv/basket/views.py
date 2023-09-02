from django.shortcuts import render

# Create your views here.
# basket/views.py

from rest_framework import viewsets
from .models import BasketItem
from .serializers import BasketItemSerializer


# class BasketViewSet(viewsets.ModelViewSet):
#     queryset = theCustomer.objects.all()
#     serializer_class = BasketSerializer


class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
