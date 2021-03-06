from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='solarPV-home'),
    path('registration/', views.registration, name='solarPV-registration'),
    path('aboutUs/', views.aboutUs, name='solarPV-aboutUs'),
    path('comingSoon/', views.comingSoon, name='solarPV-comingSoon'),
    path('webPortal/', views.webPortal, name='solarPV-webPortal'),
    path('test&cert/', views.testAndCert, name='solarPV-test&cert')

]
