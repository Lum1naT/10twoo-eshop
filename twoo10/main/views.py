from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _


from .forms import CustomerForm

# Create your views here.

## API Section ##


def api_edit_customer_personal(request):
    if(request.method == "GET"):
        return HttpResponse("This is GET, or 404")
    elif(request.method == "POST"):
        return HttpResponse("This has been posted")


## ##

## test section - delete later ##

def test(request):
    return HttpResponse("Test")

## ##

## cs Section ##


def cs_index(request):
    return render(request, 'main/index.html')


def cs_account(request):
    form = CustomerForm()
    return render(request, 'main/account_personal.html', {"form": form})


def cs_account_addresses(request):
    form = CustomerForm()
    return render(request, 'main/account_addresses.html', {"form": form})
