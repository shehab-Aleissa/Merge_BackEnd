from rest_framework import serializers
from .models import Category, Product, Order, ProductItem
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token', ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    


class CategorySerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_items(self, obj):
        items = obj.product_set.all()
        return ProductSerializer(items, many=True, context=self.context).data


class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductItem
        fields = ['quantity', 'product']


class OrderListSerialzer(serializers.ModelSerializer):
    user = UserSerializer()
    productitem_set = ProductItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ['product']
