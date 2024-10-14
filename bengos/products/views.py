from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product


def home(request):
    product=Product.objects.all().values()
    return  render(request,'home.html',{'product':product})
