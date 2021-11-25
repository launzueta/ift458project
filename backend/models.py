from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyAccountManager(BaseUserManager):
    def create_user(self, username, firstname, lastname, email, password=None):
        if not username:
            raise ValueError("Must have username")
        if not firstname:
            raise ValueError("Must have firstname")
        if not lastname:
            raise ValueError("Must have lastname")
        if not email:
            raise ValueError("Must have email")
        user = self.model(
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, firstname, lastname, email, password):
        user = self.create_user(
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Client(models.Model):
    clientID = models.CharField(max_length=50, primary_key=True, unique=True)
    clientname = models.CharField(max_length=100)
    clienttype = models.CharField(max_length=100, blank=True)


class SPVUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, unique=True)
    officephone = models.CharField(max_length=100, blank=True)
    cellphone = models.CharField(max_length=100, blank=True)
    prefix = models.CharField(max_length=10)
    clientID = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)

    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Certificate(models.Model):
    certificateNumber = models.IntegerField(primary_key=True, unique=True)
    userID = models.ForeignKey(SPVUser, on_delete=models.SET_NULL, blank=True, null=True)
    clientID = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    reportNumber = models.IntegerField(blank=True)