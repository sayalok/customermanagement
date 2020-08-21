from django.http import HttpResponse
from django.shortcuts import render

def products(request):
    return HttpResponse("Products")
