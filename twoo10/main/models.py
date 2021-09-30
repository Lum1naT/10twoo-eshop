from django.db import models
from django.db.models.aggregates import Max

# Create your models here.


COUTRY_CHOICES = (
    ('CZ', 'CZECH REPUBLIC'),
    ('DE', 'GERMANY'),
    ('AU', 'AUSTRIA'),
    ('PL', 'POLAND'),
    ('SK', 'SLOVAK REPUBLIC'),

)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    account_status = models.IntegerField()

    def __str__(self):
        return self.surname + ", " + self.name


class Address(models.Model):
    adress_line_one = models.CharField(max_length=255)
    adress_line_two = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    country = models.CharField(max_length=100, choices=COUTRY_CHOICES)
    zip_code = models.CharField(max_length=15)
    customer = models.ManyToManyField(Customer)

    def __str__(self):
        return self.country + ", " + self.adress_line_one + ", " + self.adress_line_two + ", " + self.suite


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()
    price_euro = models.FloatField()
    price_czk = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(max_length=31)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    items = models.ManyToManyField(Item)
