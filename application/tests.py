# from django.test import TestCase
# from .models import Customer, Order
# from unittest.mock import patch
# from application.send_sms import queue_sms


# class CustomerTestCase(TestCase):
#     def setUp(self):
#         self.customer = Customer.objects.create(name="Jane Doe", code="JD432", phone_number="+254799447878")

#     def test_customer_creation(self):
#         self.assertEqual(self.customer.name, "Jane Doe")
#         self.assertEqual(self.customer.code, "JD432")
#         self.assertEqual(self.customer.phone_number, "+254799447878")


# class OrderTestCase(TestCase):
#     def setUp(self):
#         self.customer = Customer.objects.create(name="Jane Doe", code="JD432", phone_number="+254799447878")
#         self.order = Order.objects.create(customer=self.customer, item="Laptop", amount=35000.00)

#     def test_order_creation(self):
#         self.assertEqual(self.order.item, "Laptop")
#         self.assertEqual(self.order.amount, 35000.00)
#         self.assertEqual(self.order.customer, self.customer)


# class SMSAlertTest(TestCase):
#     def setUp(self):
#         self.customer = Customer.objects.create(name="Jane Doe", code="JD432", phone_number="+254799447878")
    
#     @patch('application.send_sms.send_sms_alert')
#     def test_sms_alert_on_order_creation(self, mock_send_sms_alert):
#         Order.objects.create(customer=self.customer, item="Laptop", amount=35000.00)
#         queue_sms(self.customer.phone_number, "Order placed")
#         mock_send_sms_alert.assert_called_once_with("+254799447878", "Order placed")