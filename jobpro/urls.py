"""jobpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job.views import *
from superadmin.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('student_login', student_login, name="student_login"),
    path('student_signup', student_signup, name="student_signup"),
    path('student_signup_save', student_signup_save, name="student_signup_save"),
    path('student_home', student_home, name="student_home"),
    path('Logout', Logout, name="Logout"),
    path('admin_home', admin_home, name="admin_home"),
    path('view_users', view_users, name="view_users"),
    path('student_pending', student_pending, name="student_pending"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('recruiter_accepted', recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
                  # path('recruiter_all',recruiter_all,name="recruiter_all"),
    path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
    path('change_passwordstudent', change_passwordstudent, name="change_passwordstudent"),
    path('add_job', add_job, name="add_job"),
    path('job_list', job_list, name="job_list"),
                  # path('delete_recruiter/<int:pid>',delete_recruiter,name="delete_recruiter"),
    path('edit_jobdetail/<int:pid>', edit_jobdetail, name="edit_jobdetail"),
    path('latest_jobs', latest_jobs, name="latest_jobs"),
    path('student_latestjobs', student_latestjobs, name="student_latestjobs"),
    path('job_detail/<int:pid>', job_detail, name="job_detail"),
    path('applyforjob/<int:pid>', applyforjob, name="applyforjob"),
    path('applyforjob/<int:pid>', applyforjob, name="applyforjob"),
    path('applied_candidatelist', applied_candidatelist, name="applied_candidatelist"),
    path('contact', contact, name="contact"),
    path('stu', stu_login, name="stu"),
    path('rotp', Registerotp, name="rotp"),
    path('votp', verify_regotp, name="votp"),
    path('stuhome', stu_home, name="stuhome"),
    path('studup', studetailupdate, name="studup"),
    path('adminlogin', adminlogin, name="loginad"),
    path('adlog', adminlog, name="adl"),
    path('adminhome', adminhome, name="adminhome"),
    path('addjob', addjob, name="adjob"),
    path('jobaddform', jobaddform, name="jobaddform"),
    path('joblist', joblist, name="joblist"),
    path('showuser', showusers, name="showuser"),
    path('edituser', editusers, name="edituser"),
    path('edituser/<int:id>', editusers, name="edituser"),
    path('updateudetail/<int:id>', updateuserdetail, name="upud"),
    path('deleteuser', deleteuserview, name="duv"),
    path('editjob/<int:id>', editjobs, name="ejob"),
    path('updatejob/<int:id>', updatejobdetail, name="upjd"),
    path('deletejob', deletejob, name="deljob"),
    path('changepass', changepass, name="cp"),
    path('changepassword', stuchangepass, name="cpd"),
    path('jobapply', jobapplyy, name='joba'),
    path('jobde/<int:id>', job_de, name='jobd'),
    path('alljob', alljobs, name='alj'),
    path('jpl/<int:id>', jobaply, name='jp'),
    path('jobaply', jobapplied, name='joba'),
    path('deletejobcan', deletejobcan, name='djc'),
    path('payment', rrhomee, name='paym'),
    path('success', successpayment, name='succs'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
