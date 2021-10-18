"""twoo10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    ## api interface ##
    path('api/customer/personal/edit', views.api_customer_personal_edit,
         name="api_customer_personal_edit"),

    path('api/customer/register', views.api_customer_register,
         name="api_customer_register"),

    ## ##
    path('test/', views.test, name="test"),

    ## / Section ##
    path('', views.cs_index, name="cs_index"),
    path('registrace', views.cs_account_register, name="cs_account_register"),
    path('login', views.cs_account_login, name="cs_account_login"),

    path('ucet', views.cs_account, name="cs_account"),

    path('ucet/adresy', views.cs_account_addresses, name="cs_account_addresses"),

    ## End of / Section ##
]
