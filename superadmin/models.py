from django.db import models

# Create your models here.

class Addjob(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    startdate = models.CharField(max_length=500, null=True, blank=True)
    enddate = models.CharField(max_length=500, null=True, blank=True)
    salary = models.IntegerField( null=True, blank=True)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    Experience = models.IntegerField()
    company = models.CharField(max_length=500, null=True, blank=True)
    skill = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    Education = models.CharField(max_length=500, null=True, blank=True)
    Jobtype = models.CharField(max_length=500, null=True, blank=True)
    prize = models.FloatField(null=True, blank=True)
    location = models.CharField(null=True, blank=True,max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

class otpverifywithtimer(models.Model):
    email = models.EmailField(null=True, blank=True)
    otp = models.EmailField(null=True, blank=True)
    verify = models.BooleanField(default=False)

