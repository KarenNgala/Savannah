import pytest
from application.serializers import CustomerSerializer, OrderSerializer
from application.models import Customer, Order

@pytest.mark.django_db
def test_customer_serializer():
    customer_data = {'name': 'John Doe', 'phone_number': '+254799447878'}
    serializer = CustomerSerializer(data=customer_data)
    assert serializer.is_valid(), f"Errors: {serializer.errors}"
    customer = serializer.save()
    assert customer.code == "CUST001"

@pytest.mark.django_db
def test_order_serializer():
    customer = Customer.objects.create(name="Jane Doe", phone_number="+254712345679")
    order_data = {'customer': customer.id, 'item': 'Item B', 'amount': 50.00}
    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid()
    order = serializer.save()
    assert order.item == "Item B"
