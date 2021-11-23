from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps


def home(request):
    return render(request, 'solarPv/home.html')


def registration(request):
    return render(request, 'solarPv/registration.html')


def aboutUs(request):
    return render(request, 'solarPv/aboutUs.html')


def comingSoon(request):
    return render(request, 'solarPv/comingSoon.html')


def webPortal(request):
    return render(request, 'solarPv/webPortal.html')


def testAndCert(request):
    clientModel = apps.get_model('backend', 'Client')
    context = {
        'client': clientModel.objects.all()
    }
    return render(request, 'solarPv/testAndCert.html', context)