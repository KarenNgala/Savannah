import pytest
from django.urls import reverse
from unittest import mock
from django.contrib.auth.models import User
from rest_framework import status
from .conftest import CustomerFactory, OrderFactory


@pytest.mark.django_db
class TestCustomerViewSet:
    @pytest.fixture
    def authenticated_user(self, client, mocker):
        user = User.objects.create_user(username='testuser', password='password')
        mocker.patch('mozilla_django_oidc.auth.OIDCAuthenticationBackend.authenticate', return_value=user)        
        client.force_login(user)
        return client


    def test_create_customer_authenticated(self, authenticated_user):
        url = reverse('customer-list')
        customer_data = {
            'name': 'John Doe',
            'phone_number': '+254799447878'
        }
        response = authenticated_user.post(url, customer_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == customer_data['name']


    def test_create_customer_unauthenticated(self, client):
        url = reverse('customer-list')
        customer_data = {
            'name': 'Jane Doe',
            'phone_number': '+254799447878'
        }
        response = client.post(url, customer_data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN



@pytest.mark.django_db
class TestOrderViewSet:
    @pytest.fixture
    def authenticated_user(self, client, mocker):
        user = User.objects.create_user(username='testuser', password='password')        
        mocker.patch('mozilla_django_oidc.auth.OIDCAuthenticationBackend.authenticate', return_value=user)
        client.force_login(user)
        return client


    def test_create_order_authenticated(self, authenticated_user):
        customer = CustomerFactory()
        url = reverse('order-list')
        order_data = {
            'customer': customer.id,
            'item': 'Test Item',
            'amount': 100.00
        }
        response = authenticated_user.post(url, order_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['item'] == order_data['item']


    def test_create_order_unauthenticated(self, client):
        customer = CustomerFactory()
        url = reverse('order-list')
        order_data = {
            'customer': customer.id,
            'item': 'Test Item',
            'amount': 100.00
        }
        response = client.post(url, order_data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN