from django.shortcuts import render,redirect
from datetime import datetime,date
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from .filter import StudentFilter
import csv

def export_to_csv(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename="student.csv"'
    response.write('\ufeff'.encode('utf8'))
    writer.writerow(['Student','Roll ID','Phone','Guardian','GuardianPhone','Email','Address','Subjects','Course','Status'])
    student_fields = students.values_list('student','roll_id','phone','guardian','guardian_ph','email','address','subjects','course','status')
    for student in student_fields:
        writer.writerow(student)
        print(student)
    return redirect('Home')

@login_required(login_url='Login')
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'Class/register.html',{
        "form": form,
    })

@login_required(login_url='Login')
def inquery_register(request):
    form = QueryForm()
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'Class/query_register.html',{
        "form": form,
    })

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('Home')
        else:
            messages.success(request, "There Was An Error Registering. Try Again...")
            return redirect('Signup')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return redirect('login')
    return render(request,'registration/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out!"))
    return redirect('Login')

@login_required(login_url='Login')
def dashboard(request):
    student = Student.objects.all()
    lastStudent = Student.objects.order_by('-date_created').reverse()[:5]
    total_student = student.filter(status="understudies").count()
    total_complete = student.filter(status="complete").count()
    total_resign = student.filter(status="resign").count()
    inquery = Query.objects.all().count()
    context={
            'student': student,
            'total_student': total_student,
            'total_complete': total_complete,
            'total_resign': total_resign,
            'total_inquery': inquery,
            'last':lastStudent
    }
    return render(request,'Class/dashboard.html',context)
    
@login_required(login_url='Login')
def course(request):
    courses = Course.objects.all()
    context ={
        'courses':courses
    }
    return render(request,'Class/course.html',context)

@login_required(login_url='Login')
def student(request):
    student = Student.objects.all()
    student = student.filter(status="understudies").all()
    context={
        'student': student
    }
    return render(request,'Class/student.html',context)

@login_required(login_url='Login')
def inquery(request):
    people = Query.objects.all()
    return render(request,'Class/inquery.html',{'student':people})


@login_required(login_url='Login')
def dropout(request):
    student = Student.objects.all()
    student = student.filter(status="resign").all()
    #print(student)
    stud_list = []
    dictSubjects = []
    for i,_ in enumerate(student):
        stud_list.append(i)
        dictSubjects.append(list(Student.subjects.through.objects.filter(student_id=student[i].id).values())) 
    subjs = {}

    for no,dics in enumerate(dictSubjects):
        subjs[no] = []
        for i,subj in enumerate(dics):
            subjectname = Subject.objects.filter(id=subj['subject_id'])[0]
            subjs[no].append(subjectname)


    context={
        'student': student,
        'subjects': subjs
    }
    return render(request,'Class/dropout.html',context)

@login_required(login_url='Login')
def completed(request):
    student = Student.objects.all()
    student = student.filter(status="complete").all()
    return render(request,'Class/completed.html',{'student':student})

@login_required(login_url='Login')
def updateStudent(request,data):
    student = Student.objects.get(id=data)
    form = RegisterForm(instance=student)
    if request.method == "POST":
        form = RegisterForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("Home"))
    return render(request, 'Class/update_student.html',{
        "form": form,
    })

@login_required(login_url='Login')
def deleteStudent(request,data):
    item = Student.objects.get(id=data)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'Class/delete_student.html',context)

@login_required(login_url='Login')
def studentinfo(request,data):
    student = Student.objects.get(id=data)
    dictSubjects = list(Student.subjects.through.objects.filter(student_id=student.id).values())    
    subjs = []
    for i,subj in enumerate(dictSubjects):
        subjectname = Subject.objects.filter(id=subj['subject_id'])[0]
        subjs.append(subjectname)

    context = {
        'student':student,
        'rollid': student.roll_id,
        'subjects':subjs
        }
    return render(request,'Class/studentinfo.html',context)

@login_required(login_url='Login')
def queryinfo(request,data):
    student = Query.objects.get(id=data)
    dictSubjects = list(Query.subjects.through.objects.filter(query_id=student.id).values())  
    #print(dictSubjects)  
    subjs = []
    for i,subj in enumerate(dictSubjects):
        subjectname = Subject.objects.filter(id=subj['subject_id'])[0]
        subjs.append(subjectname)

    context = {
        'student':student,
        'subjects':subjs
        }
    return render(request,'Class/queryinfo.html',context)

@login_required(login_url='Login')
def querytostu(request,data):
    student = Query.objects.get(id=data)
    form = RegisterForm(instance=student)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            student.delete()
            #print(Student.objects.all())
            return HttpResponseRedirect(reverse("Home"))
    return render(request, 'Class/update_student.html',{
        "form": form,
    })

@login_required(login_url='Login')
def search(request):
    object_list  = Student.objects.all()
    search_term = request.GET.get('search')
    search_term2 = request.GET.get('search2')
    #print(object_list)
    if search_term:
        object_list = object_list.filter(student=search_term)
    if search_term2:
        object_list = object_list.filter(roll_id=search_term2)
        

    return render(request,'Class/search.html',{'object_list':object_list})

@login_required(login_url='Login')
def courseInfo(request,courseid):
    name = Course.objects.get(id=courseid)
    student = Student.objects.all()
    classStudent = student.filter(course=name)
    #print(classStudent)
    context = {
        'courseid':courseid,
        'course':name,
        'student':classStudent
    }
    return render(request,'Class/course_info.html',context) 

