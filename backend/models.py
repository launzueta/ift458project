from django.db import models


class Client(models.Model):
    clientID = models.CharField(max_length=50, primary_key=True, unique=True)
    clientname = models.CharField(max_length=100)
    clienttype = models.CharField(max_length=100, blank=True)


class SPVUser(models.Model):
    userID = models.CharField(max_length=50, primary_key=True, unique=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    officephone = models.CharField(max_length=100, blank=True)
    cellphone = models.CharField(max_length=100, blank=True)
    prefix = models.CharField(max_length=10)
    clientID = models.ManyToManyField(Client)


class Certificate(models.Model):
    certificateNumber = models.IntegerField(primary_key=True, unique=True)
    userID = models.ManyToManyField(SPVUser)
    clientID = models.ManyToManyField(Client)
    reportNumber = models.IntegerField(blank=True)




