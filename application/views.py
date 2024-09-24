from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .send_sms import send_sms_alert


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['time']
    search_fields = ['item']
    ordering_fields = ['time']

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        message = f'New order: {order.item} for {order.amount}'
        send_sms_alert(customer.phone_number, message)