from django.shortcuts import render
from backend.models import Client, Certificate


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
    if request.method == 'POST':
        search_word = request.POST.get("key", "")
        if search_word == "ALL":
            certificate_list = Certificate.objects.all()
        else:
            certificate_list = Certificate.objects.filter(clientID=search_word)
    else:
        certificate_list = Certificate.objects.all()
    return render(request, 'solarPv/testAndCert.html', {'certificate_list': certificate_list})
