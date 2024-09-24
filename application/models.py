from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super(Customer, self).save(*args, **kwargs)

    def generate_unique_code(self):
        code = f'CUST{Customer.objects.count() + 1:03}'
        return code

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item