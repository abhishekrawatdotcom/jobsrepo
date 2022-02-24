from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from superadmin.models import *

# Create your models here.

class Usermanager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser=True')

        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    username = None
    Name = models.CharField(max_length=255, null=True,blank=True )
    email = models.CharField(max_length=255, null=True,blank=True , unique=True)
    contact = models.CharField(max_length=12, null=True,blank=True)
    fname = models.CharField(max_length=255, null=True,blank=True)
    laname = models.CharField(max_length=255, null=True,blank=True)
    father = models.CharField(max_length=30, null=True,blank=True)
    mother = models.CharField(max_length=30, null=True,blank=True)
    aadhar = models.CharField(max_length=30, null=True,blank=True)
    martial = models.CharField(max_length=20, null=True,blank=True)
    age = models.CharField(max_length=10, null=True,blank=True)
    gender = models.CharField(max_length=20, null=True,blank=True)
    password = models.CharField(max_length=255, null=True,blank=True)
    address1 = models.CharField(max_length=100, null=True,blank=True)
    address2 = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    district = models.CharField(max_length=100, null=True,blank=True)
    pin = models.CharField(max_length=100,null=True,blank=True)
    tehsil = models.CharField(max_length=200, null=True,blank=True)
    nationlity = models.CharField(max_length=200, null=True,blank=True)
    caste = models.CharField(max_length=200, null=True,blank=True)
    PhysicallyHandicap = models.CharField(max_length=200, null=True,blank=True)
    economically = models.CharField(max_length=200, null=True,blank=True)
    Quata = models.CharField(max_length=200, null=True,blank=True)
    Minority = models.CharField(max_length=200, null=True,blank=True)
    tenthsc = models.CharField(max_length=200, null=True,blank=True)
    tenthpy = models.CharField(max_length=200, null=True,blank=True)
    tenthbu = models.CharField(max_length=200, null=True,blank=True)
    tenthtm = models.CharField(max_length=200, null=True,blank=True)
    tenthmo = models.CharField(max_length=200, null=True,blank=True)
    tenthpgc = models.CharField(max_length=200, null=True,blank=True)
    twelvesc = models.CharField(max_length=200, null=True, blank=True)
    twelvepy = models.CharField(max_length=200, null=True, blank=True)
    twelvebu = models.CharField(max_length=200, null=True, blank=True)
    twelvetm = models.CharField(max_length=200, null=True, blank=True)
    twelvemo = models.CharField(max_length=200, null=True, blank=True)
    twelvepgc = models.CharField(max_length=200, null=True, blank=True)
    graduationsc = models.CharField(max_length=200, null=True, blank=True)
    graduationpy = models.CharField(max_length=200, null=True, blank=True)
    graduationbu = models.CharField(max_length=200, null=True, blank=True)
    graduationtm = models.CharField(max_length=200, null=True, blank=True)
    graduationmo = models.CharField(max_length=200, null=True, blank=True)
    graduationpgc = models.CharField(max_length=200, null=True, blank=True)
    postgraduationsc = models.CharField(max_length=200, null=True, blank=True)
    postgraduationpy = models.CharField(max_length=200, null=True, blank=True)
    postgraduationbu = models.CharField(max_length=200, null=True, blank=True)
    postgraduationtm = models.CharField(max_length=200, null=True, blank=True)
    postgraduationmo = models.CharField(max_length=200, null=True, blank=True)
    postgraduationpgc = models.CharField(max_length=200, null=True, blank=True)
    Criteria = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=10, null=True,blank=True)
    month = models.CharField(max_length=10, null=True,blank=True)
    designation = models.CharField(max_length=100, null=True,blank=True)
    department = models.CharField(max_length=100, null=True,blank=True)
    companyname = models.CharField(max_length=100, null=True,blank=True)
    appointmen = models.CharField(max_length=100, null=True,blank=True)
    profilepic = models.ImageField(upload_to='profile',blank=True,null=True)
    signature = models.ImageField(upload_to='signature',blank=True,null=True)
    type = models.CharField(max_length=15, null=True,blank=True)
    verify = models.BooleanField(default=False)
    status = models.CharField(max_length=20, null=True,blank=True)
    Education = models.CharField(max_length=20, null=True,blank=True)
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Applyjobs(models.Model):
    usr = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    job = models.ForeignKey(Addjob,null=True, blank=True,on_delete=models.CASCADE)
    verify = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

