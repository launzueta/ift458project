from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'solarPv/home.html')

def registration(request):
    return render(request, 'solarPv/registration.html')

def aboutUs(request):
    return render(request, 'solarPv/aboutUs.html')

def comingSoon(request):
    return render(request, 'solarPv/comingSoon.html')