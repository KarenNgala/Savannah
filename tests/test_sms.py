import pytest
import queue
from django.urls import reverse
from unittest import mock
from django.contrib.auth.models import User
from rest_framework import status
from .conftest import CustomerFactory


@pytest.mark.django_db
class TestOrderSMS:
    @pytest.fixture
    def authenticated_user(self, client, mocker):
        user = User.objects.create_user(username='testuser', password='password')        
        mocker.patch('mozilla_django_oidc.auth.OIDCAuthenticationBackend.authenticate', return_value=user)
        client.force_login(user)
        return client

    @mock.patch('application.send_sms.sms.send')
    def test_send_sms_on_order_create(self, mock_send_sms, authenticated_user):
        customer = CustomerFactory(phone_number='+254799447878')
        url = reverse('order-list')
        
        order_data = {
            'customer': customer.id,
            'item': 'Test Item',
            'amount': 150.00
        }
        
        response = authenticated_user.post(url, order_data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED        
        assert mock_send_sms.called
        assert mock_send_sms.call_count == 1
        
        message = f"New order: Test Item for 150.00"
        mock_send_sms.assert_called_with(message, [str(customer.phone_number)])