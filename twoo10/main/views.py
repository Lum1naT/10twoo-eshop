from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def cs_index(request):
    return render(request, 'main/cs/index.html')


def cs_account(request):
    return render(request, 'main/cs/account.html')
