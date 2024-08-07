from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'login-django.html')

def register_view(request):
    return render(request, 'register-django.html')

def home_view(request):
    return render(request, 'home.html')