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
            if(email_already_registered != 0):
                pass  # email already exists in DB

            # TODO: Messaging system and redirects
            # settings
            must_contain_lowercase = True
            must_contain_uppercase = True
            must_contain_number = True
            must_contain_special = True
            required_length = 6
            # variables
            contains_lowercase = False
            contains_uppercase = False
            contains_number = False
            contains_special = False
            # sets of characters
            special_characters = "!@#$%^&*()-+?_=,<>/\""
            lowercase_set = "abcdefghijklmnopqrstuvwxyz"
            uppercase_set = lowercase_set.upper()
            number_set = "1234567890"

            password_length = len(data.get("password"))
            if(password_length < required_length):
                # Error: password is not long enough
                return HttpResponse("Password is not long enough.")

            passwords_match = (data.get("password") ==
                               data.get("password_check"))
            if(not passwords_match):
                # Error: passwords mismatch
                return HttpResponse("Passwords mismatch.")

            # here goes the logic explanation of this code:
            # first, we define settings, variables stay False for now
            if(must_contain_lowercase):  # if this is True, then the corresponging contains_smthing variable must be true as well, if it is False, both will always stay False
                if any(c in lowercase_set for c in data.get("password")):
                    contains_lowercase = True

            if(must_contain_uppercase):
                if any(c in uppercase_set for c in data.get("password")):
                    contains_uppercase = True

            if(must_contain_special):
                if any(c in special_characters for c in data.get("password")):
                    contains_special = True

            if(must_contain_number):
                if any(c in number_set for c in data.get("password")):
                    contains_number = True
            # after all of this, we check if True == True or False == False, otherwise - the password does not meet the requirements
            if(must_contain_number == contains_number and must_contain_lowercase == contains_lowercase and must_contain_uppercase == contains_uppercase and must_contain_special == contains_special):
                # password check ok.
                pass
            else:
                return HttpResponse("password NOT OK.")

            if(True):
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
        # TODO: redirect to account or mainpage
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
