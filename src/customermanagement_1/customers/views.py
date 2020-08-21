from django.http import HttpResponse
from django.shortcuts import render

def customers(request):
    return render(request, "pages/test.html", {})
