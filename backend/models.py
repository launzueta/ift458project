from django.db import models


class Client(models.Model):
    cleintID = models.CharField(max_length=50, primary_key=True, unique=True)
    clientname = models.CharField(max_length=100)
    clienttype = models.CharField(max_length=100)


class TestSequence(models.Model):
    sequenceID = models.CharField(max_length=50, primary_key=True, unique=True)
    sequencename = models.CharField(max_length=100)


class TestStandard(models.Model):
    standardID = models.CharField(max_length=50, primary_key=True, unique=True)
    standardname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    punlisheddate = models.DateField()


class Product(models.Model):
    modelnumber = models.CharField(max_length=50, primary_key=True, unique=True)
    productname = models.CharField(max_length=100)
    celltechnology = models.CharField(max_length=100)
    cellmanufacturer = models.CharField(max_length=100)
    numberofcells = models.CharField(max_length=100)
    numberofcellsinseries = models.CharField(max_length=100)
    numberofseriesstrings = models.CharField(max_length=100)
    numberofdiodes = models.CharField(max_length=100)
    productlength = models.CharField(max_length=100)
    productwidth = models.CharField(max_length=100)
    productweight = models.CharField(max_length=100)
    superstatetype = models.CharField(max_length=100)
    superstatemanufacturer = models.CharField(max_length=100)
    substratetype = models.CharField(max_length=100)
    substratemanufacturer = models.CharField(max_length=100)
    frametype = models.CharField(max_length=100)
    frameadhesive = models.CharField(max_length=100)
    encapsulatetype = models.CharField(max_length=100)
    enacapsulatemanufacturer = models.CharField(max_length=100)
    junctionboxtype = models.CharField(max_length=100)
    junctionboxmanufacturer = models.CharField(max_length=100)


class User(models.Model):
    userID = models.CharField(max_length=50, primary_key=True, unique=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    email = models.EmailField()
    officephone = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=100)
    prefix = models.CharField(max_length=10)
    clientID = models.ManyToManyField(Client)


class Location(models.Model):
    locationID = models.CharField(max_length=50, primary_key=True, unique=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    faxnumber = models.CharField(max_length=100)
    clientID = models.ManyToManyField(Client)


class Service(models.Model):
    serviceID = models.IntegerField(primary_key=True, unique=True)
    servicename = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isFIrequired = models.BooleanField()
    FIfrequency = models.IntegerField()
    standardID = models.ForeignKey(TestStandard, on_delete=models.CASCADE())


class PerformanceData(models.Model):
    modelnumber = models.ForeignKey(Product, on_delete=models.CASCADE())
    sequenceID = models.ForeignKey(TestStandard, on_delete=models.CASCADE())
    maxsystemvoltage = models.IntegerField()
    voc = models.IntegerField()
    isc = models.IntegerField()
    vmp = models.IntegerField()
    imp = models.IntegerField()
    pmp = models.IntegerField()
    ff = models.IntegerField()


class Certificate(models.Model):
    certificateNumber = models.IntegerField(primary_key=True, unique=True)
    userID = models.ManyToManyField(User)
    reportNumber = models.IntegerField()
    issueDate = models.DateField()
    standardID = models.ForeignKey(TestStandard, on_delete=models.CASCADE())
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE())
    modelnumber = models.ForeignKey(Product, on_delete=models.CASCADE())



