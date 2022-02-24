from django.shortcuts import render
from datetime import date

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import uuid
import datetime
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
user = get_user_model()
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from superadmin.models import *


def adminlog(request):
    return render(request,'admin/login.html')

def adminlogin(request):
    print('ttttt')
    if request.method == 'POST':
        email = request.POST.get('emailad')
        password = request.POST.get('passwordad')
        print('rrrr')

        if user.objects.filter(email=email).exists():
            user_obj = authenticate(request, email=email, password=password)
            if user_obj is not None:
                if user_obj.is_superuser == True and user_obj.is_staff == True:
                    login(request, user_obj)
                    return redirect('/adminhome')

            else:
                messages.error(request, 'You have entered incorrect password')
                return redirect('')
        else:
            messages.error(request, 'This email is not exists')
            return redirect('')

    return redirect('/ooooooooo')


def adminhome(request):
    userlen = user.objects.filter(is_superuser=False).count()
    return render(request,'admin/admin_home.html',{'userlen':userlen})

def addjob(request):
    return render(request,'admin/addjob.html')

def jobaddform(request):
    if request.method == 'POST':
        title = request.POST.get('addjobtitle')
        sdate = request.POST.get('addstartdate')
        edate = request.POST.get('addenddate')
        salary = request.POST.get('addsalary')
        logo = request.FILES.get('addlogo')
        experience = request.POST.get('addexperience')
        company = request.POST.get('addlocation')
        skill = request.POST.get('addskills')
        desc = request.POST.get('adddescription')
        education = request.POST.get('adddeducation')
        jobtype = request.POST.get('adddjobtype')
        add = Addjob(title=title,startdate=sdate,enddate=edate,salary=salary,logo=logo,Experience=experience,company=company,skill=skill,description=desc,Education=education,Jobtype=jobtype)
        add.save()
        messages.success(request,'Successfully added job')
        return redirect('/addjob')

def joblist(request):
    alljobs = Addjob.objects.all().order_by('-id')
    return render(request,'admin/joblist.html',{'alljobs':alljobs})

def showusers(request):
    allusers = user.objects.filter(is_superuser=False)
    return render(request,'admin/studentview.html',{'allusers':allusers})

def editusers(request,id):
    userid = user.objects.get(id=id)
    return render(request,'admin/editusers.html',{'userid':userid})

def updateuserdetail(request,id):
    u = user.objects.get(id=id)
    u.fname = request.POST.get('usefname')
    u.laname= request.POST.get('uselname')
    u.save()
    return redirect('/showuser')

def deleteuserview(request):
    dd = request.GET.get('id')
    print(dd, 'myobjid')
    d = user.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true': True})


def editjobs(request,id):
    ejob = Addjob.objects.get(id=id)
    return render(request,'admin/editjob.html',{'ejob':ejob})

def updatejobdetail(request,id):
    u = Addjob.objects.get(id=id)
    u.company = request.POST.get('jorganization')
    u.Experience= request.POST.get('jexp')
    u.skill= request.POST.get('jskil')
    u.Education= request.POST.get('jedu')
    u.Jobtype= request.POST.get('jjtype')
    u.salary= request.POST.get('jsalary')
    u.save()
    return redirect('/joblist')


def deletejob(request):
    dd = request.GET.get('id')
    print(dd, 'myobjid')
    d = Addjob.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def changepass(request):
    return render(request,'admin/changepassword.html')



