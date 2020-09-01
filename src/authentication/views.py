from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages

def loginUser(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect("authentication:dashboard")
            else:
                messages.info(request,"Username Or Password Not Match")
        else:
            messages.info(request,"Not Valid Data")
    else:
        loginForm = LoginForm()
        
    data = {'loginForm':loginForm}
    return render(request, "pages/login.html", data)

def logoutUser(request):
    logout(request)
    loginForm = LoginForm()
    data = {'loginForm':loginForm}
    return redirect("authentication:login")

def dashboard(request):
    return render(request, "pages/dashboard.html", {})