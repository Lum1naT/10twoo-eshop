from django.contrib import admin
from .models import Customer, Address
from django.utils.translation import gettext as _


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")


