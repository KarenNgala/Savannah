from rest_framework import serializers
from .models import Customer, Order
from phonenumber_field.serializerfields import PhoneNumberField


class CustomerSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()
    
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'