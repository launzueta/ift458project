from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('client/', views.ClientListView.as_view(), name='client_list'),
    path('client/<pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('spvuser/', views.SPVUserListView.as_view(), name='spvuser_list'),
    path('spvuser/<pk>/', views.SPVUserDetailView.as_view(), name='spvuser_detail'),
    path('certificate/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificate/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
]
