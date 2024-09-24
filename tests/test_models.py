import pytest
from application.models import Customer, Order

@pytest.mark.django_db
def test_customer_creation():
    customer = Customer(name="John Doe", phone_number="+254712345678")
    customer.save()
    assert customer.code == "CUST001"
    assert str(customer) == "John Doe"

@pytest.mark.django_db
def test_order_creation():
    customer = Customer.objects.create(name="Jane Doe", phone_number="+254712345679")
    order = Order.objects.create(customer=customer, item="Item A", amount=99.99)
    assert order.customer == customer
    assert str(order) == "Item A"
