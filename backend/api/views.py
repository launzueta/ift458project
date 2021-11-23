from rest_framework import generics
from ..models import Client, SPVUser, Certificate
from .serializers import ClientSerializer, SPVUserSerializer, CertificateSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SPVUserListView(generics.ListAPIView):
    queryset = SPVUser.objects.all()
    serializer_class = SPVUserSerializer


class SPVUserDetailView(generics.RetrieveAPIView):
    queryset = SPVUser.objects.all()
    serializer_class = SPVUserSerializer


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateDetailView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
