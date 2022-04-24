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
import uuid
from threading import Timer
from django.contrib.auth.decorators import login_required
# Create your views here.


def finddata(request):
    return render(request,'finddata.html')



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
                return redirect('/student_login')
        else:
            messages.error(request, 'This email is not exists')
            return redirect('/student_login')

    return redirect('/pro')

def jobapplyy(request):
    return render(request,'jobapplyy.html')

def job_de(request,id):
    jd = Addjob.objects.get(id=id)
    return render(request,'jobdetail.html',{'job':jd})

def jobaply11(request,id):
    request.session['payid1'] = id
    usr = request.user
    aj = Addjob.objects.get(id=id)
    if Applyjobs.objects.filter(usr=usr,job=aj).exists():
        messages.info(request, 'You Alredy Applied to the job')
    else:
        return redirect('/payment1')
    return redirect('/alljob')



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

    try:
        u_email = request.user.email
        u = user.objects.get(email=u_email)
        c = u.department
        alj = Addjob.objects.filter(Education__icontains=c)

    except:
        return redirect('')

    return render(request,'student_latestjobs.html',{'alj':alj})


def student_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
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
    amount1 = jobprize
    request.session['amount'] = amount1

    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'payment.html',{'payment':payment})

def rrhomee1(request):
    pay11 = request.session['payid1']

    al = Addjob.objects.get(id=pay11)
    jobprize = al.prize
    print(pay11)
    amount = jobprize*100
    amount1 = jobprize
    request.session['amount1'] = amount1
    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'payment1.html',{'payment':payment})


def successpayment(request):
    response = request.POST
    param_dict = {
        "razorpay_payment_id":response['razorpay_payment_id'],
        "razorpay_order_id":response['razorpay_order_id'],
        "razorpay_signature":response['razorpay_signature'],
    }
    print(param_dict)

    try:
        if response['razorpay_signature']:
            pay11 = request.session['payid']
            amont = request.session['amount']
            usr = request.user
            aj = Addjob.objects.get(id=pay11)
            Applyjobs.objects.create(job=aj, usr=usr,paymentid=response['razorpay_payment_id'],orderid=response['razorpay_order_id'],paid=amont)
            uid = uuid.uuid4()
            u_email = request.user.email
            u = user.objects.get(email=u_email)
            u.Criteria = uid
            u.save()
            messages.info(request, 'Successfully Applied to the job')
            return redirect('/alljob')
    except:
        return redirect('/payment/')




def successpayment1(request):
    response = request.POST
    param_dict = {
        "razorpay_payment_id": response['razorpay_payment_id'],
        "razorpay_order_id": response['razorpay_order_id'],
        "razorpay_signature": response['razorpay_signature'],
    }
    print(param_dict)

    try:
        if response['razorpay_signature']:
            pay11 = request.session['payid1']
            amount1 = request.session['amount1']
            usr = request.user
            aj = Addjob.objects.get(id=pay11)
            Applyjobs.objects.create(job=aj, usr=usr,paymentid=response['razorpay_payment_id'],orderid=response['razorpay_order_id'],paid=amount1)
            uid = uuid.uuid4()
            u_email = request.user.email
            u = user.objects.get(email=u_email)
            u.Criteria = uid
            u.save()
            messages.info(request, 'Successfully Applied to the job')
            return redirect('/alljob')
    except:
        return redirect('/payment1/')







def Registerotp(request):
    return render(request,'regotpverify.html')


# @csrf_exempt
# def verify_regotp(request):
# 	if request.method == 'POST':
# 		otp = request.POST.get('otp1')
# 		try:
# 		    otp_2 = request.session['otp1']
# 		except KeyError:
# 		    messages.info(request, 'Incorrect OTP Entered')
# 		    return redirect('/rotp')
#
# 		try:
# 			if otp == otp_2:
# 				return redirect('/student_login')
# 			else:
# 				messages.info(request, 'Incorrect OTP Entered')
# 				return redirect('/rotp')
# 		except KeyError:
# 			return redirect('/rotp')


@csrf_exempt
def verify_regotp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp1')
        s = request.session['emailca11']

        if otpverifywithtimer.objects.filter(otp=otp,email=s).exists():
            return redirect('/student_signup')
        else:
            messages.info(request, 'Incorrect OTP Entered')
            return redirect('/rotp')




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
        u.tehsil = request.POST.get('tehsil11')
        u.district = request.POST.get('district11')
        u.nationlity = request.POST.get('nationality11')
        u.Minority = request.POST.get('minority11')
        u.gender = request.POST.get('gender')
        u.caste = request.POST.get('caste11')
        u.PhysicallyHandicap = request.POST.get('physicallyhandicap11')
        u.city = request.POST.get('city11')
        u.pin = request.POST.get('pin11')
        u.tenth = request.POST.get('tenth11')
        u.twelve = request.POST.get('twelve11')
        u.economically = request.POST.get('economically11')
        u.Quata = request.POST.get('quota11')
        u.tenthsc = request.POST.get('tenth11')
        u.tenthpy = request.POST.get('tenth12')
        u.tenthbu = request.POST.get('tenth13')
        u.tenthtm = request.POST.get('tenth14')
        u.tenthmo = request.POST.get('tenth15')
        u.tenthpgc = request.POST.get('tenth16')
        u.twelvesc = request.POST.get('twelve11')
        u.twelvepy = request.POST.get('twelve12')
        u.twelvebu = request.POST.get('twelve13')
        u.twelvetm = request.POST.get('twelve14')
        u.twelvemo = request.POST.get('twelve15')
        u.twelvepgc = request.POST.get('twelve16')
        u.graduationsc = request.POST.get('graduation11')
        u.graduationpy = request.POST.get('graduation12')
        u.graduationbu = request.POST.get('graduation13')
        u.graduationtm = request.POST.get('graduation14')
        u.graduationmo = request.POST.get('graduation15')
        u.graduationpgc = request.POST.get('graduation16')
        u.postgraduationsc = request.POST.get('postgraduation11')
        u.postgraduationpy = request.POST.get('postgraduation12')
        u.postgraduationbu = request.POST.get('postgraduation13')
        u.postgraduationtm = request.POST.get('postgraduation14')
        u.postgraduationmo = request.POST.get('postgraduation15')
        u.postgraduationpgc = request.POST.get('postgraduation16')
        u.year = request.POST.get('year11')
        u.month = request.POST.get('month11')
        u.designation = request.POST.get('designation11')
        u.department = request.POST.get('department11')
        u.appointmen = request.POST.get('appointmen11')
        u.companyname = request.POST.get('organization11')
        u.academic = request.POST.get('academic11')
        u.experience = request.POST.get('experience11')
        u.profilepic = request.FILES.get('image11')
        u.signature = request.FILES.get('sing11')
        u.save()
    return redirect('/stuhome')








def admin_login(request):
    return render(request, 'admin_login.html')





def student_signup(request):
    try:
        a = request.session['contact11']
        b = request.session['emailca11']
        print('a',a)
        print('b',b)

    except:
        return redirect('/homesite')


    return render(request, 'student_signup1.html',{'a':a,"b":b})



def student_signup11(request):
    return render(request, 'student_signup2.html')



def emailcheckverify(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        request.session['emailca11'] = email
        if user.objects.filter(email=email).exists():
            messages.info(request, 'Email is already exists')
            return redirect('/homesite')
        else:
            contact = request.POST.get("contact")
            request.session['contact11'] = contact
            otp = str(
                uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
            otp = otp[0:6]
            if not otpverifywithtimer.objects.filter(email=email).exists():
                otpm = otpverifywithtimer.objects.create(otp=otp, email=email)
                otpm.save()

                # here otp update for user by resending otp , if otp already exists
            if otpverifywithtimer.objects.filter(email=email).exists():
                otpm = otpverifywithtimer.objects.get(email=email)
                otpm.otp = otp
                otpm.save()

            request.session['otp1'] = otp

            def delunverifyotp():
                if otpverifywithtimer.objects.filter(email=request.session['emailca']).exists():
                    otpm = otpverifywithtimer.objects.get(email=request.session['emailca'])
                    otpm.delete()

            t = Timer(80.0, delunverifyotp)
            t.start()
            sub = 'Welcome to Placement Portal'
            msg = '''Hi there!
                        You have successfully registered at StudentJobportal. Please confirm your account with below OTP,
                        ''' + str(otp)
            EmailMessage(sub, msg, to=[email]).send()
            messages.success(request,
                             'Registered Successfully!! Please verify your account with the OTP we have sent on your e-mail.OTP will be expired in 60 second')
        return redirect('/rotp')

def student_signup_save(request):
    print('yesss calling')
    if request.method == 'POST':
        contact = request.session['contact11']
        email = request.session['emailca11']
        if user.objects.filter(email=email).exists():
            messages.info(request, 'Email is already exists')
            return redirect('/homesite')
        print('yess  calllling')
        print('hkjkgjhkghjg')
        ufname = request.POST.get("fname")
        umiddlename = request.POST.get("mname")
        ulaname = request.POST.get("lname")
        print('jj',ufname)
        ufather = request.POST.get("father")
        umother = request.POST.get("mother")
        uidentity_desc = request.POST.get("identitydd")
        passport = request.POST.get("passport")
        pancard = request.POST.get("pancard")
        driving = request.POST.get("driving")
        umartial = request.POST.get("marital")
        uage = request.POST.get("age")
        ugender = request.POST.get("gender")
        upassword = request.POST.get("pwd11")
        ucpassword = request.POST.get("cpwd")
        uaddress1 = request.POST.get("add1")
        uaddress2 = request.POST.get("add2")
        ulandmark = request.POST.get("landmark1")
        ustate = request.POST.get("state")
        udomicial = request.POST.get("domicile")
        udomicial_certificate = request.POST.get("certificateno")
        udomicial_date = request.POST.get("issuedate")
        udomicial_district = request.POST.get("domidistrict")
        ucity = request.POST.get("city1")
        udistrict = request.POST.get("district1")
        upin = request.POST.get("zipcode1")
        utehsil = request.POST.get("tehsil1")
        unationlity = request.POST.get("nationality")
        ucaddress1 = request.POST.get("cadd")
        ucaddress2 = request.POST.get("cadd1")
        uclandmark = request.POST.get("clandmark")
        ucpin = request.POST.get("czip")
        uccity = request.POST.get("ccity")
        ucdistrict = request.POST.get("cdistrict")
        uctehsil = request.POST.get("ctehsil")
        ucstate = request.POST.get("state1")
        ucnationlity = request.POST.get("cnationality")
        ueconomically = request.POST.get("economically")
        ucaste = request.POST.get("caste")
        uPhysicallyHandicap = request.POST.get("physicallyhandicap")

        uQuata = request.POST.get("quota")
        uMinority = request.POST.get("minority")
        uqualification = request.POST.get("qualification")

        usscuniversity = request.POST.get("ssc1")
        ussccollege = request.POST.get("ssc2")
        usscdate = request.POST.get("ssc3")
        ussctotalmarks = request.POST.get("ssc4")
        usscobtainmarks = request.POST.get("ssc5")
        usscgrade = request.POST.get("ssc6")
        usscdoc = request.FILES.get("ssc7")

        uhscuniversity = request.POST.get("hsc1")
        uhsccollege = request.POST.get("hsc2")
        uhscdate = request.POST.get("hsc3")
        uhsctotalmarks = request.POST.get("hsc4")
        uhscobtainmarks = request.POST.get("hsc5")
        uhscgrade = request.POST.get("hsc6")
        uhscdoc = request.FILES.get("hsc7")

        ugraduationuniversity = request.POST.get("graduation_sc")
        ugraduationcollege = request.POST.get("graduation_py")
        ugraduationdate = request.POST.get("graduation_bu")
        ugraduationtotalmarks = request.POST.get("graduation_tm")
        ugraduationobtainmarks = request.POST.get("graduation_mo")
        ugraduationgrade = request.POST.get("graduation_pgc")
        ugraduationdoc = request.FILES.get("graduationimg")

        upostgraduationuniversity = request.POST.get("postgraduation_sc")
        upostgraduationcollege = request.POST.get("postgraduation_py")
        upostgraduationdate = request.POST.get("postgraduation_bu")
        upostgraduationtotalmarks = request.POST.get("postgraduation_tm")
        upostgraduationobtainmarks = request.POST.get("postgraduation_mo")
        upostgraduationgrade = request.POST.get("postgraduation_pgc")
        upostgraduationdoc = request.FILES.get("postgradimg")

        uphduniversity = request.POST.get("phd_bu")
        uphdcollege = request.POST.get("phd_py")
        uphddate = request.POST.get("phd_bh")
        uphdtotalmarks = request.POST.get("phd_tm")
        uphdobtainmarks = request.POST.get("phd_mo")
        uphdgrade = request.POST.get("phd_pgc")
        uphddoc = request.POST.get("phd_img")



        uyear = request.POST.get("year")
        umonth = request.POST.get("month")
        udesignation = request.POST.get("designation")
        udepartment = request.POST.get("department")
        ucompanyname = request.POST.get("organization")
        uappointmen = request.POST.get("appointmen")
        usalary = request.POST.get("salary1")
        uexpectedsalary = request.POST.get("salary2")
        uprofilepic = request.FILES.get('profilepic')
        usignature = request.FILES.get('signature')
        print(ufname,unationlity)
        # u = user(Name=name, email=email,middlename=middlename, contact=contact, fname=fname, laname=lname, father=father,
        #                          mother=mother, aadhar=aadhar, martial=marital, age=age, gender=gender,password=make_password(password),
        #                           address1=address1, address2=address2, state=state,
        #                          city=city, pin=pin,district=district,tehsil=tehsil,nationlity=nationality,caste=caste,economically=economically,
        #                           year=year, month=month, designation=designation,PhysicallyHandicap=physicallyhandicap,Quata=quota,Minority=minority,
        #                           tenthsc=tenth_sc,tenthpy=tenth_py,tenthbu=tenth_bu,tenthmo=tenth_mo,tenthtm=tenth_tm,tenthpgc=tenth_pgc,
        #                           twelvesc=twelve_sc,twelvepy=twelve_py,twelvebu=twelve_bu,twelvetm=twelve_tm,twelvemo=twelve_mo,twelvepgc=twelve_pgc,
        #                           graduationsc=graduation_sc,graduationpy=graduation_py,graduationbu=graduation_bu,graduationtm=graduation_tm,
        #                           graduationmo=graduation_mo,graduationpgc=graduation_pgc,postgraduationsc=postgraduation_sc,postgraduationpy=postgraduation_py,
        #                           postgraduationbu=postgraduation_bu,postgraduationtm=postgraduation_tm,postgraduationmo=postgraduation_mo,
        #                           postgraduationpgc=postgraduation_pgc,companyname=companyname,appointmen=appointmen,
        #                          department=department,profilepic=profile,signature=signature)
        u = user(email=email,contact=contact,fname=ufname,laname=ulaname,father=ufather,mother=umother,
                 aadhar=uidentity_desc,martial=umartial,age=uage,gender=ugender,password=make_password(upassword),cpassword=ucpassword,
                 address1=uaddress1,address2=uaddress2,landmark=ulandmark,state=ustate,city=ucity,district=udistrict,pin=upin,tehsil=utehsil,
                 nationlity=unationlity,domicial=udomicial,domicial_certificate=udomicial_certificate,domicial_date=udomicial_date,domicial_district=udomicial_district,
                 caddress1=ucaddress1,caddress2=ucaddress2,clandmark=uclandmark,cstate=ucstate,ccity=uccity,cdistrict=ucdistrict,cpin=ucpin,
                 ctehsil=uctehsil,cnationlity=ucnationlity,caste=ucaste,PhysicallyHandicap=uPhysicallyHandicap,economically=ueconomically,
                 Quata=uQuata,Minority=uMinority,qualification=uqualification,sscuniversity=usscuniversity,ssccollege=ussccollege,sscdate=usscdate,
                 ssctotalmarks=ussctotalmarks,sscobtainmarks=usscobtainmarks,sscgrade=usscgrade,sscdoc=usscdoc,hscuniversity=uhscuniversity,
                 hsccollege=uhsccollege,hscdate=uhscdate,hsctotalmarks=uhsctotalmarks,hscobtainmarks=uhscobtainmarks,hscgrade=uhscgrade,
                 hscdoc=uhscdoc,graduationuniversity=ugraduationuniversity,graduationcollege=ugraduationcollege,graduationdate=ugraduationdate,
                 graduationtotalmarks=ugraduationtotalmarks,graduationobtainmarks=ugraduationobtainmarks,graduationgrade=ugraduationgrade,
                 graduationdoc=ugraduationdoc,postgraduationuniversity=upostgraduationuniversity,postgraduationcollege=upostgraduationcollege,
                 postgraduationdate=upostgraduationdate,postgraduationtotalmarks=upostgraduationtotalmarks,postgraduationobtainmarks=upostgraduationobtainmarks,
                 postgraduationgrade=upostgraduationgrade,postgraduationdoc=upostgraduationdoc,phduniversity=uphduniversity,phdcollege=uphdcollege,
                 phddate=uphddate,phdtotalmarks=uphdtotalmarks,phdobtainmarks=uphdobtainmarks,phdgrade=uphdgrade,phddoc=uphddoc,year=uyear,
                 month=umonth,designation=udesignation,department=udepartment,companyname=ucompanyname,appointmen=uappointmen,
                 salary=usalary,expectedsalary=uexpectedsalary,profilepic=uprofilepic,passport=passport,pancard=pancard,drivinglicens=driving,signature=usignature,middlename=umiddlename)
        u.save()
        messages.success(request,'you are successfully Registered')
        return redirect('/student_login')



# def student_signup_save(request):,
#     print('yesss calling')
#     if request.method == 'POST':
#         a = request.session['contact11']
#         b = request.session['emailca11']
#         print('yess  calllling')
#         u = user.objects.get(email='abhi00@gmail.com')
#         print('hkjkgjhkghjg')
#         u.fname = request.POST.get("fname")
#         u.middlename = request.POST.get("mname")
#         u.laname = request.POST.get("lname")
#         print('jj',u.fname)
#         u.father = request.POST.get("father")
#         u.mother = request.POST.get("mother")
#         u.identity_detail = request.POST.get("identity")
#         u.identity_desc = request.POST.get("identitydd")
#         u.martial = request.POST.get("marital")
#         u.age = request.POST.get("age")
#         u.gender = request.POST.get("gender")
#         u.password = request.POST.get("pwd11")
#         u.cpassword = request.POST.get("cpwd")
#         u.address1 = request.POST.get("add1")
#         u.address2 = request.POST.get("add2")
#         u.landmark = request.POST.get("landmark1")
#         u.state = request.POST.get("state")
#         u.domicial = request.POST.get("domicile")
#         u.domicial_certificate = request.POST.get("certificateno")
#         u.domicial_date = request.POST.get("issuedate")
#         u.domicial_district = request.POST.get("domidistrict")
#         u.city = request.POST.get("city1")
#         u.district = request.POST.get("district1")
#         u.pin = request.POST.get("zipcode1")
#         u.tehsil = request.POST.get("tehsil1")
#         u.nationlity = request.POST.get("nationality")
#         u.caddress1 = request.POST.get("cadd")
#         u.caddress2 = request.POST.get("cadd1")
#         u.clandmark = request.POST.get("clandmark")
#         u.cpin = request.POST.get("czip")
#         u.ccity = request.POST.get("ccity")
#         u.cdistrict = request.POST.get("cdistrict")
#         u.ctehsil = request.POST.get("ctehsil")
#         u.cstate = request.POST.get("state1")
#         u.cnationlity = request.POST.get("cNationality")
#         u.economically = request.POST.get("economically")
#         u.caste = request.POST.get("caste")
#         u.PhysicallyHandicap = request.POST.get("physicallyhandicap")
#
#         u.Quata = request.POST.get("quota")
#         u.Minority = request.POST.get("minority")
#         u.qualification = request.POST.get("qualification")
#
#         u.sscuniversity = request.POST.get("ssc1")
#         u.ssccollege = request.POST.get("ssc2")
#         u.sscdate = request.POST.get("ssc3")
#         u.ssctotalmarks = request.POST.get("ssc4")
#         u.sscobtainmarks = request.POST.get("ssc5")
#         u.sscgrade = request.POST.get("ssc6")
#         u.sscdoc = request.FILES.get("ssc7")
#
#         u.hscuniversity = request.POST.get("hsc1")
#         u.hsccollege = request.POST.get("hsc2")
#         u.hscdate = request.POST.get("hsc3")
#         u.hsctotalmarks = request.POST.get("hsc4")
#         u.hscobtainmarks = request.POST.get("hsc5")
#         u.hscgrade = request.POST.get("hsc6")
#         u.hscdoc = request.FILES.get("hsc7")
#
#         u.graduationuniversity = request.POST.get("graduation_sc")
#         u.graduationcollege = request.POST.get("graduation_py")
#         u.graduationdate = request.POST.get("graduation_bu")
#         u.graduationtotalmarks = request.POST.get("graduation_tm")
#         u.graduationobtainmarks = request.POST.get("graduation_mo")
#         u.graduationgrade = request.POST.get("graduation_pgc")
#         u.graduationdoc = request.FILES.get("graduationimg")
#
#         u.postgraduationuniversity = request.POST.get("postgraduation_sc")
#         u.postgraduationcollege = request.POST.get("postgraduation_py")
#         u.postgraduationdate = request.POST.get("postgraduation_bu")
#         u.postgraduationtotalmarks = request.POST.get("postgraduation_tm")
#         u.postgraduationobtainmarks = request.POST.get("postgraduation_mo")
#         u.postgraduationgrade = request.POST.get("postgraduation_pgc")
#         u.postgraduationdoc = request.FILES.get("postgradimg")
#
#         u.phduniversity = request.POST.get("phd_bu")
#         u.phdcollege = request.POST.get("phd_py")
#         u.phddate = request.POST.get("phd_bh")
#         u.phdtotalmarks = request.POST.get("phd_tm")
#         u.phdobtainmarks = request.POST.get("phd_mo")
#         u.phdgrade = request.POST.get("phd_pgc")
#         u.phddoc = request.POST.get("phd_img")
#
#
#
#         u.year = request.POST.get("year")
#         u.month = request.POST.get("month")
#         u.designation = request.POST.get("designation")
#         u.department = request.POST.get("department")
#         u.companyname = request.POST.get("organization")
#         u.appointmen = request.POST.get("appointmen")
#         u.salary = request.POST.get("salary1")
#         u.expectedsalary = request.POST.get("salary2")
#         u.profilepic = request.FILES.get('profilepic')
#         u.signature = request.FILES.get('signature')
#         print(u.fname,u.nationlity)
#         # u = user(Name=name, email=email,middlename=middlename, contact=contact, fname=fname, laname=lname, father=father,
#         #                          mother=mother, aadhar=aadhar, martial=marital, age=age, gender=gender,password=make_password(password),
#         #                           address1=address1, address2=address2, state=state,
#         #                          city=city, pin=pin,district=district,tehsil=tehsil,nationlity=nationality,caste=caste,economically=economically,
#         #                           year=year, month=month, designation=designation,PhysicallyHandicap=physicallyhandicap,Quata=quota,Minority=minority,
#         #                           tenthsc=tenth_sc,tenthpy=tenth_py,tenthbu=tenth_bu,tenthmo=tenth_mo,tenthtm=tenth_tm,tenthpgc=tenth_pgc,
#         #                           twelvesc=twelve_sc,twelvepy=twelve_py,twelvebu=twelve_bu,twelvetm=twelve_tm,twelvemo=twelve_mo,twelvepgc=twelve_pgc,
#         #                           graduationsc=graduation_sc,graduationpy=graduation_py,graduationbu=graduation_bu,graduationtm=graduation_tm,
#         #                           graduationmo=graduation_mo,graduationpgc=graduation_pgc,postgraduationsc=postgraduation_sc,postgraduationpy=postgraduation_py,
#         #                           postgraduationbu=postgraduation_bu,postgraduationtm=postgraduation_tm,postgraduationmo=postgraduation_mo,
#         #                           postgraduationpgc=postgraduation_pgc,companyname=companyname,appointmen=appointmen,
#         #                          department=department,profilepic=profile,signature=signature)
#         u.save()
#         return redirect('/rotp')


        # otp = str(
        #     uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
        # otp = otp[0:6]
        # if not otpverifywithtimer.objects.filter(email=email).exists():
        #     otpm = otpverifywithtimer.objects.create(otp=otp, email=email)
        #     otpm.save()
        #
        #     # here otp update for user by resending otp , if otp already exists
        # if otpverifywithtimer.objects.filter(email=email).exists():
        #     otpm = otpverifywithtimer.objects.get(email=email)
        #     otpm.otp = otp
        #     otpm.save()
        #
        #
        # request.session['otp1'] = otp
        #
        # def delunverifyotp():
        #     if otpverifywithtimer.objects.filter(email=request.session['emailca']).exists():
        #         otpm = otpverifywithtimer.objects.get(email=request.session['emailca'])
        #         otpm.delete()
        #
        # t = Timer(80.0, delunverifyotp)
        # t.start()
        # sub = 'Welcome to Placement Portal'
        # msg = '''Hi there!
        #         You have successfully registered at StudentJobportal. Please confirm your account with below OTP,
        #         ''' + str(otp) + "  " + "\nEmail id:" + email +"  " + "\nPassword:" + password
        # EmailMessage(sub, msg, to=[email]).send()
        # messages.success(request,
        #                  'Registered Successfully!! Please verify your account with the OTP we have sent on your e-mail.')
    # return redirect('/rotp')





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


@csrf_exempt
def forgotpassword(request):
	return render(request,'forgotemail.html')

def forgot_otp(request):
	return render(request,'forgototp.html')

@csrf_exempt
def check_email(request):
	if request.method == 'POST':
		email = request.POST.get('myemail')
		if not user.objects.filter(email=email).exists():
			messages.success(request, 'email is not exist with this email')
			return redirect('/forgotpass')

		else:
			otp = str(uuid.uuid5(uuid.NAMESPACE_DNS,str(datetime.datetime.today()) + email ).int)
			otp = otp[0:6]
			request.session['forgotp'] = otp
			request.session['emailid'] = user.objects.get(email=email).id
			sub = 'Job Portal - Password Change Request'
			msg = ''' Hi there!
We received a password change request, please verify your email with below OTP.
'''+str(otp)
			EmailMessage(sub, msg, to=[email]).send()
			messages.success(request, 'An OTP has been sent to your email.')
			return redirect('/forgot-otp')
	return HttpResponse('bossss')

@csrf_exempt
def verify_forgot(request):
	if request.method == 'POST':
		otp = request.POST.get('forotp')
		otp_2 = request.session['forgotp']
		try:
			if otp == otp_2:
				return redirect('/addpassw')
			else:
				messages.info(request, 'Incorrect OTP Entered')
				return redirect('/forgot-otp')
		except KeyError:
			return HttpResponse('Error')

@csrf_exempt
def change_password(request):
	if request.method == 'POST':
		setpwd = request.POST.get('mypass')
		userid = request.session['emailid']
		user1 = user.objects.get(id=userid)
		user1.set_password(setpwd)
		user1.save()
		messages.success(request, 'Password Changed Successfully !!!!')
		return redirect('/student_login')
	else:
		return render(request, 'forgotaddpassword.html')


