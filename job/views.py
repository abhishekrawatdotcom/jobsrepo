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
import razorpay
# Create your views here.


def stu_login(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        password = request.POST.get('password1')

        if user.objects.filter(email=email).exists():
            user_obj = authenticate(request, email=email, password=password)
            if user_obj is not None:
                login(request, user_obj)
                return redirect('/stuhome')


            else:
                messages.error(request, 'You have entered incorrect password')
                return redirect('')
        else:
            messages.error(request, 'This email is not exists')
            return redirect('')

    return redirect('/pro')

def jobapplyy(request):
    return render(request,'jobapplyy.html')

def job_de(request,id):
    jd = Addjob.objects.get(id=id)
    return render(request,'jobdetail.html',{'job':jd})


def jobaply(request,id):
    request.session['payid'] = id
    usr = request.user
    aj = Addjob.objects.get(id=id)
    if Applyjobs.objects.filter(usr=usr,job=aj).exists():
        messages.info(request, 'You Alredy Applied to the job')
    else:
        return redirect('/payment')
    return redirect('/alljob')

'''
aj = Addjob.objects.get(id=id)
Applyjobs.objects.create(job=aj, usr=usr)
messages.info(request, 'Successfully Applied to the job')
'''

def jobapplied(request):
    uu = Applyjobs.objects.all()
    return render(request,'jobapplied.html',{'apj':uu})

def deletejobcan(request):
    dd = request.GET.get('id')
    print(dd, 'myobjid')
    d = Applyjobs.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})


def alljobs(request):
    if request.method == 'POST':

        amount = 500000
        currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_i1xzsJR2FTEV1a', 'xnwm66CZgdssJdnNSQcDSQWt'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    aljjj = request.POST.get('hideaply')
    print(aljjj)

    u_email = request.user.email
    u = user.objects.get(email=u_email)
    c = u.Criteria
    alj = Addjob.objects.filter(Education__icontains=c)
    return render(request,'student_latestjobs.html',{'alj':alj})


def student_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST['email'];
        password = request.POST['password'];
        user = authenticate(email=email, password=password)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}

    return render(request, 'student_login.html', d)


def rrhomee(request):
    pay11 = request.session['payid']
    al = Addjob.objects.get(id=pay11)
    jobprize = al.prize
    print(pay11)
    amount = jobprize*100
    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'payment.html',{'payment':payment})

def successpayment(request):
    pay11 = request.session['payid']
    usr = request.user
    aj = Addjob.objects.get(id=pay11)
    Applyjobs.objects.create(job=aj, usr=usr)
    messages.info(request, 'Successfully Applied to the job')
    return redirect('/alljob')


def Registerotp(request):
    return render(request,'regotpverify.html')

@csrf_exempt
def verify_regotp(request):
	if request.method == 'POST':
		otp = request.POST.get('otp1')
		otp_2 = request.session['otp1']
		try:
			if otp == otp_2:
				return redirect('/dashboard/')
			else:
				messages.info(request, 'Incorrect OTP Entered')
				return redirect('/rotp')
		except KeyError:
			return HttpResponse('Error')


def index(request):
    return render(request, 'index.html')


def stu_home(request):
    u_email = request.user.email
    u = user.objects.get(email=u_email)
    return render(request,'stuhome.html',{'u':u})

def stuchangepass(request):
    u_email = request.user.email
    u = user.objects.get(email=u_email)
    u.set_password(request.POST.get('newpass'))
    u.save()
    return redirect('')

def studetailupdate(request):
    if request.method == 'POST':
        u_email = request.user.email
        u = user.objects.get(email=u_email)
        u.Name = request.POST.get('name11')
        u.email = request.POST.get('email11')
        u.contact = request.POST.get('contact11')
        u.fname = request.POST.get('fname11')
        u.laname = request.POST.get('laname11')
        u.father = request.POST.get('father11')
        u.mother = request.POST.get('mother11')
        u.aadhar = request.POST.get('aadhar11')
        u.martial = request.POST.get('martial11')
        u.age = request.POST.get('age11')
        u.address1 = request.POST.get('address111')
        u.address2 = request.POST.get('address211')
        u.state = request.POST.get('state11')
        u.city = request.POST.get('city11')
        u.pin = request.POST.get('pin11')
        u.tenth = request.POST.get('tenth11')
        u.twelve = request.POST.get('twelve11')
        u.graduation = request.POST.get('graduation11')
        u.postgraduation = request.POST.get('postgraduation11')
        u.year = request.POST.get('year11')
        u.month = request.POST.get('month11')
        u.designation = request.POST.get('designation11')
        u.department = request.POST.get('father11')
        u.academic = request.POST.get('academic11')
        u.experience = request.POST.get('experience11')
        u.profilepic = request.FILES.get('image11')
        u.signature = request.FILES.get('sing11')
        u.tenmrk = request.FILES.get('ten11')
        u.twelvemrk = request.FILES.get('twel11')
        u.graduationmrk = request.FILES.get('grad11')
        u.postgraduationmrk = request.FILES.get('postgrad11')
        u.save()
    return redirect('/hhhh')








def admin_login(request):
    return render(request, 'admin_login.html')





def student_signup(request):
    return render(request, 'student_signup.html')


def student_signup_save(request):
    if request.method == 'POST':
        print('hkjkgjhkghjg')
        name = request.POST.get("username")
        print(name)
        email = request.POST.get("email")
        print(email)
        contact = request.POST.get("contact")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        father = request.POST.get("father")
        mother = request.POST.get("mother")
        aadhar = request.POST.get("aadhar")
        marital = request.POST.get("marital")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        password = make_password(request.POST.get("pwd11"))
        address1 = request.POST.get("address1")
        address2 = request.POST.get("adress2")
        state = request.POST.get("state")
        city = request.POST.get("city")
        district = request.POST.get("district")
        pin = request.POST.get("pin")
        tehsil = request.POST.get("tehsil")
        nationality = request.POST.get("nationality")
        caste = request.POST.get("caste")
        physicallyhandicap = request.POST.get("physicallyhandicap")
        economically = request.POST.get("economically")
        quota = request.POST.get("quota")
        minority = request.POST.get("minority")
        tenth_sc = request.POST.get("tenth_sc")
        tenth_py = request.POST.get("tenth_py")
        tenth_bu = request.POST.get("tenth_bu")
        tenth_tm = request.POST.get("tenth_tm")
        tenth_mo = request.POST.get("tenth_mo")
        tenth_pgc = request.POST.get("tenth_pgc")
        twelve_sc = request.POST.get("twelve_sc")
        twelve_py = request.POST.get("twelve_py")
        twelve_bu = request.POST.get("twelve_bu")
        twelve_tm = request.POST.get("twelve_tm")
        twelve_mo = request.POST.get("twelve_mo")
        twelve_pgc = request.POST.get("twelve_pgc")
        graduation_sc = request.POST.get("graduation_sc")
        graduation_py = request.POST.get("graduation_py")
        graduation_bu = request.POST.get("graduation_bu")
        graduation_tm = request.POST.get("graduation_tm")
        graduation_mo = request.POST.get("graduation_mo")
        graduation_pgc = request.POST.get("graduation_pgc")
        postgraduation_sc = request.POST.get("postgraduation_sc")
        postgraduation_py = request.POST.get("postgraduation_py")
        postgraduation_bu = request.POST.get("postgraduation_bu")
        postgraduation_tm = request.POST.get("postgraduation_tm")
        postgraduation_mo = request.POST.get("postgraduation_mo")
        postgraduation_pgc = request.POST.get("postgraduation_pgc")
        year = request.POST.get("year")
        month = request.POST.get("month")
        designation = request.POST.get("designation")
        department = request.POST.get("department")
        companyname = request.POST.get("companyname")
        appointmen = request.POST.get("appointmen")
        profile = request.FILES.get('profilepic')
        signature = request.FILES.get('signature')
        print(name,email,contact)
        u = user(Name=name, email=email, contact=contact, fname=fname, laname=lname, father=father,
                                 mother=mother, aadhar=aadhar, martial=marital, age=age, gender=gender,password=password,
                                  address1=address1, address2=address2, state=state,
                                 city=city, pin=pin,district=district,tehsil=tehsil,nationlity=nationality,caste=caste,economically=economically,
                                  year=year, month=month, designation=designation,PhysicallyHandicap=physicallyhandicap,Quata=quota,Minority=minority,tenthsc=tenth_sc,tenthpy=tenth_py,tenthbu=tenth_bu,tenthmo=tenth_mo,tenthtm=tenth_tm,tenthpgc=tenth_pgc,twelvesc=twelve_sc,twelvepy=twelve_py,twelvebu=twelve_bu,twelvetm=twelve_tm,twelvemo=twelve_mo,twelvepgc=twelve_pgc,graduationsc=graduation_sc,graduationpy=graduation_py,graduationbu=graduation_bu,graduationtm=graduation_tm,graduationmo=graduation_mo,graduationpgc=graduation_pgc,postgraduationsc=postgraduation_sc,postgraduationpy=postgraduation_py,postgraduationbu=postgraduation_bu,postgraduationtm=postgraduation_tm,postgraduationmo=postgraduation_mo,postgraduationpgc=postgraduation_pgc,companyname=companyname,appointmen=appointmen,
                                 department=department,profilepic=profile,signature=signature)
        u.save()


        otp = str(
            uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
        otp = otp[0:6]
        request.session['otp1'] = otp
        sub = 'Welcome to Pickleman'
        msg = '''Hi there!
                You have successfully registered at StudentJobportal. Please confirm your account with below OTP,
                ''' + str(otp)
        EmailMessage(sub, msg, to=[email]).send()
        messages.success(request,
                         'Registered Successfully!! Please verify your account with the OTP we have sent on your e-mail.')
    return redirect('/rotp')





def student_home(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    return render(request, 'student_home.html')


def Logout(request):
    logout(request)
    return redirect('index')


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}

    return render(request, 'admin_login.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    scount = StudentUser.objects.all().count()
    d = {'scount': scount}
    return render(request, 'admin_home.html', d)


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_users.html', d)


def student_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.filter(status='pending')
    d = {'data': data}
    return render(request, 'student_pending.html', d)


def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    student = StudentUser.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['status']
        student.status = s
        try:
            student.save()
            error = "no"
        except:
            error = "yes"
    d = {'student': student, 'error': error}
    return render(request, 'change_status.html', d)


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordadmin.html', d)


def change_passwordstudent(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordstudent.html', d)


def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.filter(status='Accept')
    d = {'data': data}
    return render(request, 'recruiter_accepted.html', d)


def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.filter(status='Reject')
    d = {'data': data}
    return render(request, 'recruiter_rejected.html', d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        lg = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        admin = Admin.objects.get(user=user)

        try:
            Job.objects.create(admin=admin, start_date=sd, end_date=ed, title=jt, salary=sal, image=lg,
                               description=des, experience=exp, location=loc, skills=skills, creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_job.html', d)


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    admin = Admin.objects.get(user=user)
    job = Job.objects.filter(admin=admin)
    d = {'job': job}
    return render(request, 'job_list.html', d)


def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    job = Job.objects.get(id=pid)

    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des

        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass

        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass

    d = {'error': error, 'job': job}
    return render(request, 'edit_jobdetail.html', d)


def change_companylogo(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    job = Job.objects.get(id=pid)

    if request.method == 'POST':
        cl = request.FILES['logo']

        job.image = cl

        try:
            job.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'job': job}
    return render(request, 'change_companylogo.html', d)


def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'latest_jobs.html', d)


def job_detail(request, pid):
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_detail.html', d)


def student_latestjobs(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li = []
    for i in data:
        li.append(i.job.id)

    d = {'job': job, 'li': li}
    return render(request, 'student_latestjobs.html', d)


def applyforjob(request, pid):
    if not request.user.is_authenticated:
        return redirect('student_login')
    error = ""
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    if job.end_date < date1:
        error = "closed"
    elif job.start_date > date1:
        error = "notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job, student=student, resume=r, applydate=date.today())
            error = "done"
    d = {'error': error}
    return render(request, 'applyforjob.html', d)


def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    data = Apply.objects.all()

    d = {'data': data}
    return render(request, 'applied_candidatelist.html', d)


def contact(request):
    return render(request, 'contact.html')


