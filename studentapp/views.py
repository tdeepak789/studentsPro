from django.shortcuts import render, redirect
from studentapp.stuforms import StudentRegister,srchform,stuLoginForm,StudentUpdateForm,Staff as StaffForm
from studentapp.models import StudentRegister as sr,Staff as staffRegister

from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def view(request):
    return render(request,'base.html')
def register(request):
    title = "New Student Registration Form"
    ack = "Registered Successfully"
    if request.method=="POST":
        form1 = StudentRegister(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['s_name']
            # attendance = form1.cleaned_data['s_attendance']
            contact = form1.cleaned_data['s_contact']
            section = form1.cleaned_data['s_section']

            # age = form1.cleaned_data['s_age']
            clas = form1.cleaned_data['s_class']
            email = form1.cleaned_data['s_email']
            pswd = form1.cleaned_data['s_password']
            temp = sr(s_name=name,s_class=clas,s_email=email,s_password=pswd,s_contact=contact,s_section=section)
            temp.save()
            ack = ack + "Your Registration Number is :"+str(temp.s_reg)
            return render(request,'stuack.html',{'ack':ack})
    else:
        form1 = StudentRegister()
        return render(request,'register.html',{'title':title ,'form':form1})
def home(request):
    return render(request,'home.html')
        
    
def registered(request):
    title="All Registered Students"
    result = sr.objects.all()
    return render(request,'view.html',{'result':result,'title':title})

def search(request):
    title="Your search results"

    form1 =srchform(request.POST or None)
    # name = form.cleaned_data['sname']
    if request.method=="POST":
        form1 = srchform(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['sname']
            result = sr.objects.all().filter(s_name=name)
            if len(result)==0:
                return render(request,'ack.html',{'ack':"Student not found"})
            return render(request,'view.html',{'title':title,'result':result})
    
    return render(request,'search.html',{'form':form1,'title':"Search For Student"})
def delete(request):
    title="Your search results"

    form1 =srchform(request.POST or None)
    # name = form.cleaned_data['sname']
    if request.method=="POST":
        form1 = srchform(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['sname']
            result = sr.objects.all().filter(s_name=name)
            if len(result)==0:
                return render(request,'ack.html',{'ack':"Student not found"})
            result = sr.objects.all().filter(s_name=name).delete()
            return render(request,'ack.html',{'ack':"Student Deleted Success Fully"})
        return render(request,'delete.html',{'form':form1,'title':"Search For Student"})
    
    return render(request,'delete.html',{'form':form1,'title':"Search For Student"})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return render(request,'base.html')  # Redirect to Django admin dashboard
        else:
            messages.error(request, 'Invalid login credentials or insufficient permissions.')
    
    return render(request, 'admin_login.html')

def studentLogin(request):
    title="Your search results"

    form1 =stuLoginForm(request.POST or None)
    # name = form.cleaned_data['sname']
    if request.method=="POST":
        form1 = stuLoginForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['s_name']
            pwd = form1.cleaned_data['s_password']
            result = sr.objects.all().filter(s_name=name)
            if len(result)==0:
                return render(request,'stuack.html',{'ack':"Student not found"})
            for i in result:
                if(int(i.s_password)==int(pwd)):
                    return render(request,'stuview.html',{'result':result,'title':"Your Data"})
            return render(request,'stulogin.html',{'form':form1,'title':"Student Login Page Password Invalid"})
        return render(request,'stulogin.html',{'form':form1,'title':"Student Login Page"}) 
    return render(request,'stulogin.html',{'form':form1,'title':"Student Login Page"})

def update(request):
    ack = "Enter Student name to search"
    if request.method == "POST":
        form1 = srchform(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['sname']
            result = sr.objects.filter(s_name=name)
            if len(result) == 0:
                return render(request, 'ack.html', {'ack': "Student not found"})
            form = StudentUpdateForm(request.POST)
            return render(request, 'updatestudentform.html', {'ack': "update student details", 'form': form,'name':name})
        return render(request, 'updatesearch.html', {'form': form1,'ack':ack})
    else:
        form1 = srchform()
        return render(request, 'updatesearch.html', {'form': form1,'ack':ack})

def updatestudent(request,name):
    if request.method =="POST":
        form = StudentUpdateForm(request.POST)
        if form.is_valid():
            attendance = form.cleaned_data['s_attendance']
            contact = form.cleaned_data['s_contact']
            section = form.cleaned_data['s_section']
            fees = form.cleaned_data['s_feedue'] 
            clas = form.cleaned_data['s_class']
            email = form.cleaned_data['s_email']
            pswd = form.cleaned_data['s_password']
            try:
                sr.objects.filter(s_name=name).update(s_attendance=attendance, s_feedue=fees, s_section=section, s_class=clas)
                sr.save()
                form.save()
            except Exception as e:
                print(f"Error updating the record: {e}")
            return render(request, 'ack.html', {'ack': "Updated Successfully"})
        return render(request, 'updatestudentform.html', {'ack': "update student details", 'form': form})
    return render(request, 'updatestudentform.html', {'ack': "update student details", 'form': form})
    # ack = "Update the student Details for " + name
    
def addStaff(request):
    title = "New Staff Registration Form"
    ack = "Registered Successfully"
    if request.method=="POST":
        form1 = StaffForm(request.POST)
        if form1.is_valid():
            name     = form1.cleaned_data['staff_name']
            subjects = form1.cleaned_data['staff_subjects']
            sections = form1.cleaned_data['staff_sections']
            email    = form1.cleaned_data['staff_email']
            pswd     = form1.cleaned_data['staff_password']
            temp     = staffRegister(staff_name=name,staff_subjects=subjects,staff_sections=sections,staff_email=email,staff_password=pswd)
            temp.save()
            ack = ack + "Your Registration Number is :"+str(temp.staff_id)
            return render(request,'stuack.html',{'ack':ack})
    else:
        form1 = StaffForm()
        return render(request,'register.html',{'title':title ,'form':form1})