from django.db import models
from django.db.models.aggregates import Max
from django.utils.translation import gettext as _
from django.utils import timezone
from django.core.validators import RegexValidator


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


COUTRY_CHOICES = (
    ('CZ', _('Czech Republic')),
    ('DE', _('Germany')),
    ('AU', _('Austria')),
    ('PL', _('Poland')),
    ('SK', _('Slovak Republic')),

)


GENDER_CHOICES = (
    ('F', _('Female')),
    ('M', _('Male')),
    ('U', _('Undefined')),
)

ADDRESS_TYPE_CHOICES = (
    ('S', _('Shipping')),
    ('B', _('Billing')),
    ('U', _('Undefined')),
)


class Customer(models.Model):
    name = models.CharField(_("Name"), max_length=100,  blank=True, null=True)
    surname = models.CharField(
        _("Surname"), max_length=100,  blank=True, null=True)
    email = models.EmailField(_("Email"),  blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+12345678915'. Up to 15 digits allowed.")
    phone_number = models.CharField(_("Phone number"),                                  validators=[
                                    phone_regex], max_length=17, blank=True, null=True)  # validators should be a list

    date_of_birth = models.DateField(
        _("Date of birth"),  blank=True, null=True)
    gender = models.CharField(_("Gender"),
                              max_length=10, choices=GENDER_CHOICES, default="U",  blank=True, null=True)
    account_status = models.IntegerField(
        _("Account status"), default=1)

    last_updated = AutoDateTimeField(default=timezone.now, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.surname + ", " + self.name


class Address(models.Model):
    adress_line_one = models.CharField(max_length=255)
    adress_line_two = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    country = models.CharField(max_length=100, choices=COUTRY_CHOICES)
    zip_code = models.CharField(max_length=15)
    customer = models.ManyToManyField(Customer)
    type = models.CharField(
        max_length=100, choices=ADDRESS_TYPE_CHOICES, default="U")
    last_updated = AutoDateTimeField(default=timezone.now, editable=False)
    created_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return self.country + ", " + self.adress_line_one + ", " + self.adress_line_two + ", " + self.zip_code


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()
    price_euro = models.DecimalField(max_digits=10, decimal_places=2)
    price_czk = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = AutoDateTimeField(default=timezone.now, editable=False)
    created_at = models.DateField(default=timezone.now, editable=False)
    category = models.ManyToManyField(Category) # todo? maybe make a foreing key once we figure out what to do on_delete
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(max_length=31)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    items = models.ManyToManyField(Item)
    last_updated = AutoDateTimeField(default=timezone.now, editable=False)
    created_at = models.DateField(default=timezone.now, editable=False)
