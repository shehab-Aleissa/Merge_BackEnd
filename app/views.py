from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer, OrderListSerialzer, RegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Category, Order, ProductItem
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MakingOrder(APIView):
    def post(self, request, *args, **kwargs):
        order_obj = Order.objects.create(user=request.user)
        for order in request.data:
            product_id = order.get('id')
            quantity = order.get('quantity')
            product_obj = Product.objects.get(id=product_id)
            productItem = ProductItem.objects.create(
                order=order_obj, product=product_obj, quantity=quantity)
            return Response(status=status.HTTP_201_CREATED)


class OrderList(ListAPIView):
    query_set = Order.objects.all()
    serializer_class = OrderListSerialzer


class UserOrder(APIView):
    def get(self, request, *args, **kwargs):
        user_orders = Order.objects.get(user=request.user.id)
        serializer = OrderListSerialzer(user_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
