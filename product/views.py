from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from product.models import Product

def index(request):
    setting = Setting.objects.get(pk=1)
    return HttpResponse("Product Page")

