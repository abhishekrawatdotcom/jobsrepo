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
    middlename = models.CharField(max_length=255, null=True,blank=True )
    email = models.CharField(max_length=255, null=True,blank=True , unique=True)
    contact = models.CharField(max_length=12, null=True,blank=True)
    fname = models.CharField(max_length=255, null=True,blank=True)
    laname = models.CharField(max_length=255, null=True,blank=True)
    father = models.CharField(max_length=30, null=True,blank=True)
    mother = models.CharField(max_length=30, null=True,blank=True)
    aadhar = models.CharField(max_length=50, null=True,blank=True)
    passport = models.CharField(max_length=50, null=True,blank=True)
    pancard = models.CharField(max_length=50, null=True,blank=True)
    drivinglicens = models.CharField(max_length=50, null=True,blank=True)
    martial = models.CharField(max_length=20, null=True,blank=True)
    age = models.CharField(max_length=10, null=True,blank=True)
    gender = models.CharField(max_length=20, null=True,blank=True)
    password = models.CharField(max_length=255, null=True,blank=True)
    cpassword = models.CharField(max_length=255, null=True,blank=True)
    address1 = models.CharField(max_length=100, null=True,blank=True)
    address2 = models.CharField(max_length=100, null=True,blank=True)
    landmark = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    district = models.CharField(max_length=100, null=True,blank=True)
    pin = models.CharField(max_length=100,null=True,blank=True)
    tehsil = models.CharField(max_length=200, null=True,blank=True)
    nationlity = models.CharField(max_length=200, null=True,blank=True)
    domicial = models.CharField(max_length=200, null=True,blank=True)
    domicial_certificate = models.CharField(max_length=200, null=True,blank=True)
    domicial_date = models.CharField(max_length=200, null=True,blank=True)
    domicial_district = models.CharField(max_length=200, null=True,blank=True)
    caddress1 = models.CharField(max_length=100, null=True, blank=True)
    caddress2 = models.CharField(max_length=100, null=True, blank=True)
    clandmark = models.CharField(max_length=100, null=True, blank=True)
    cstate = models.CharField(max_length=100, null=True, blank=True)
    ccity = models.CharField(max_length=100, null=True, blank=True)
    cdistrict = models.CharField(max_length=100, null=True, blank=True)
    cpin = models.CharField(max_length=100, null=True, blank=True)
    ctehsil = models.CharField(max_length=200, null=True, blank=True)
    cnationlity = models.CharField(max_length=200, null=True, blank=True)
    caste = models.CharField(max_length=200, null=True,blank=True)
    PhysicallyHandicap = models.CharField(max_length=200, null=True,blank=True)
    economically = models.CharField(max_length=200, null=True,blank=True)
    Quata = models.CharField(max_length=200, null=True,blank=True)
    Minority = models.CharField(max_length=200, null=True,blank=True)
    qualification = models.CharField(max_length=200, null=True,blank=True)
    sscuniversity = models.CharField(max_length=200, null=True,blank=True)
    ssccollege = models.CharField(max_length=200, null=True,blank=True)
    sscdate = models.CharField(max_length=200, null=True,blank=True)
    ssctotalmarks = models.CharField(max_length=200, null=True,blank=True)
    sscobtainmarks= models.CharField(max_length=200, null=True,blank=True)
    sscgrade = models.CharField(max_length=200, null=True,blank=True)
    sscdoc = models.ImageField(upload_to='sscdoc', null=True,blank=True)

    hscuniversity = models.CharField(max_length=200, null=True, blank=True)
    hsccollege = models.CharField(max_length=200, null=True, blank=True)
    hscdate = models.CharField(max_length=200, null=True, blank=True)
    hsctotalmarks = models.CharField(max_length=200, null=True, blank=True)
    hscobtainmarks = models.CharField(max_length=200, null=True, blank=True)
    hscgrade = models.CharField(max_length=200, null=True, blank=True)
    hscdoc = models.ImageField(upload_to='hscdoc', null=True, blank=True)

    graduationuniversity = models.CharField(max_length=200, null=True, blank=True)
    graduationcollege = models.CharField(max_length=200, null=True, blank=True)
    graduationdate = models.CharField(max_length=200, null=True, blank=True)
    graduationtotalmarks = models.CharField(max_length=200, null=True, blank=True)
    graduationobtainmarks = models.CharField(max_length=200, null=True, blank=True)
    graduationgrade = models.CharField(max_length=200, null=True, blank=True)
    graduationdoc = models.ImageField(upload_to='graduationdoc', null=True, blank=True)

    postgraduationuniversity = models.CharField(max_length=200, null=True, blank=True)
    postgraduationcollege = models.CharField(max_length=200, null=True, blank=True)
    postgraduationdate = models.CharField(max_length=200, null=True, blank=True)
    postgraduationtotalmarks = models.CharField(max_length=200, null=True, blank=True)
    postgraduationobtainmarks = models.CharField(max_length=200, null=True, blank=True)
    postgraduationgrade = models.CharField(max_length=200, null=True, blank=True)
    postgraduationdoc = models.ImageField(upload_to='postgraduationdoc', null=True, blank=True)

    phduniversity = models.CharField(max_length=200, null=True, blank=True)
    phdcollege = models.CharField(max_length=200, null=True, blank=True)
    phddate = models.CharField(max_length=200, null=True, blank=True)
    phdtotalmarks = models.CharField(max_length=200, null=True, blank=True)
    phdobtainmarks = models.CharField(max_length=200, null=True, blank=True)
    phdgrade = models.CharField(max_length=200, null=True, blank=True)
    phddoc = models.ImageField(upload_to='phddoc', null=True, blank=True)

    year = models.CharField(max_length=10, null=True,blank=True)
    month = models.CharField(max_length=10, null=True,blank=True)
    designation = models.CharField(max_length=100, null=True,blank=True)
    department = models.CharField(max_length=100, null=True,blank=True)
    companyname = models.CharField(max_length=100, null=True,blank=True)
    appointmen = models.CharField(max_length=100, null=True,blank=True)
    salary = models.CharField(max_length=100, null=True,blank=True)
    expectedsalary = models.CharField(max_length=100, null=True,blank=True)

    moreyear = models.CharField(max_length=10, null=True,blank=True)
    moremonth = models.CharField(max_length=10, null=True,blank=True)
    moredesignation = models.CharField(max_length=100, null=True,blank=True)
    moredepartment = models.CharField(max_length=100, null=True,blank=True)
    morecompanyname = models.CharField(max_length=100, null=True,blank=True)
    moreappointmen = models.CharField(max_length=100, null=True,blank=True)
    moresalary = models.CharField(max_length=100, null=True,blank=True)
    moreexpectedsalary = models.CharField(max_length=100, null=True,blank=True)
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
    paymentid = models.CharField(null=True, blank=True,max_length=500)
    paid = models.CharField(null=True, blank=True,max_length=500)
    orderid = models.CharField(null=True, blank=True,max_length=500)
    verify = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

