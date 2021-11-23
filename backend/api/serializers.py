from rest_framework import serializers
from ..models import Client, SPVUser, Certificate


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['clientID', 'clientname', 'clienttype']


class SPVUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPVUser
        fields = ['userID', 'firstname', 'middlename', 'lastname', 'jobtitle', 'email',
                  'officephone', 'cellphone', 'prefix', 'clientID']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificateNumber', 'userID', 'clientID', 'reportNumber']
