from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password, CryptPasswordHasher

from .models import Customer
from .forms import CustomerForm, LoginForm, RegisterForm

# TODO: Use messaging system for errors
# Create your views here.

## API Section ##


def api_customer_personal_edit(request):
    if(request.method == "GET"):
        return HttpResponse("This is GET, or 404")
    elif(request.method == "POST"):
        return HttpResponse("This has been posted")


def api_customer_register(request):
    if(request.method == "GET"):
        return HttpResponse("This is GET, or 404")
    elif(request.method == "POST"):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            # register form is valid
            email_already_registered = Customer.objects.filter(
                email=data.get("email")).count()  # reutrns count of given email already in DB
            # TODO: password security check
            if((data.get("password") == data.get("password_check")) and email_already_registered == 0):
                # passwords match and email is unique
                new_customer = Customer()
                new_customer.name = data.get("name")
                new_customer.surname = data.get("surname")
                new_customer.email = data.get("email")
                password = data.get("password")
                hashed_password = make_password(
                    password)
                new_customer.password = hashed_password

                # always save
                new_customer.save()
            else:
                return HttpResponse("Passwords mismatch.")

            pass
        return HttpResponse("This has been posted")

## ##

## test section - delete later ##


def test(request):
    return HttpResponse("Test")

## ##

## cs Section ##


def cs_index(request):
    return render(request, 'main/index.html')


def cs_account_register(request):
    form = RegisterForm()
    return render(request, 'main/account_register.html', {"form": form})


def cs_account_login(request):
    form = LoginForm()
    return render(request, 'main/account_login.html', {"form": form})


def cs_account(request):
    form = CustomerForm()
    return render(request, 'main/account_personal.html', {"form": form})


def cs_account_addresses(request):
    form = CustomerForm()
    return render(request, 'main/account_addresses.html', {"form": form})
