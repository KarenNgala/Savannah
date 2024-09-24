import pytest
import factory
from application.models import Customer, Order
import random


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    @factory.lazy_attribute
    def phone_number(self):
        return f'+2547{random.randint(10000000, 99999999)}'


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    item = factory.Faker('word')
    amount = factory.Faker('random_number', digits=5)
