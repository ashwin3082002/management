from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from database.models import *
from utilities.functions import send_email
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')

# Authentication Views
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid Credentials!")
                return redirect('login')
        except:
            messages.error(request, "Something Wrong with Database!! Please Try Again Later")
            return redirect('login')
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('index')

# Teacher Views
@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='index')
def teacher_add(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        classes = request.POST['classes']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        try:
            teacher = Teacher.objects.create(
                full_name=full_name,
                age=age,
                date_of_birth=date_of_birth,
                classes=classes,
                email=email,
                phone_number=phone_number
            )
            teacher.save()
            teacher_id = Teacher.objects.get(email=email).id
        except:
            messages.error(request, "Something Wrong with Database!! Please Try Again Later")
            return redirect('teacher_add')
        
        flag = send_email(
            "Teacher Created Successfully! | Management Portal",
            f""" 
Hello {full_name},

You have been added as a teacher in the Management Portal, Below are the recorded details

Teacher ID: {teacher_id}
Full Name: {full_name}
Age: {age}
Date of Birth: {date_of_birth}
Contact No: {phone_number}
Email: {email}

If you find anything discripensies, Please contact the Portal Admin.

Regards,
Management Portal Team
            """,
            email
        )

        if flag:
            messages.success(request, "Teacher added successfully!")
            return redirect('teacher_view')
        else:
            messages.error(request, f"Mail Not Sent, but teacher created with ID: {teacher_id} ")
            return redirect('teacher_view')
        
    return render(request, 'teacher/teachers_add.html')

@login_required(login_url='index')
def teacher_view(request):
    teachers = Teacher.objects.all()
    if not teachers:
        messages.error(request,"No Teachers Added Yet!!")
        return redirect("teacher_view")
    
    total_no_of_classes = 0
    for teacher in teachers:
        total_no_of_classes += int(teacher.classes)
    no_of_teachers = Teacher.objects.count()
    average_no_of_classes = total_no_of_classes/no_of_teachers

    return render(request, 'teacher/teachers_view.html', {"teachers":teachers, "total_no_of_classes":total_no_of_classes, "average_no_of_classes":average_no_of_classes})

@login_required(login_url='index')
def teacher_edit(request, id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        classes = request.POST['classes']
        phone_number = request.POST['phone_number']

        try:
            teacher = Teacher.objects.get(id=id)
            teacher.full_name = full_name
            teacher.age = age
            teacher.date_of_birth = date_of_birth
            teacher.classes = classes
            teacher.phone_number = phone_number
            teacher.save()
            flag = send_email(
                "Teacher Updated Successfully! | Management Portal",
                f"""
Hello {full_name},

Your details have been updated in the Management Portal, Below are the recorded details

Teacher ID: {id}
Full Name: {full_name}
Age: {age}
Date of Birth: {date_of_birth}
Contact No: {phone_number}
Email: {teacher.email}

If you find anything discripensies, Please contact the Portal Admin.

Regards,
Management Portal Team
""",
                teacher.email)
            
            if flag:
                messages.success(request, "Teacher Updated Successfully!")
                return redirect('teacher_view')
            else:
                messages.error(request, "Teacher Updated Successfully, but mail not sent!!")
                return redirect('teacher_view')

        except:
            messages.error(request, "Something Wrong with Database!! Please Try Again Later")
            return redirect('teacher_view')

        return redirect('teacher_view')
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher/teachers_edit.html',{'teacher':teacher})

@login_required(login_url='index')
def teacher_delete(request, id):
    teacher = Teacher.objects.get(id=id)
    email = teacher.email
    name = teacher.full_name
    teacher.delete()
    flag = send_email(
        "Teacher Deleted Successfully! | Management Portal",
        f"""
Hello {name},

Your details have been deleted from the Management Portal by the admin.

If you think this is a mistake, Please contact the Portal Admin.

Regards,
Management Portal Team
""",
        email)
    
    if flag:   
        messages.success(request, "Teacher Deleted Successfully!")
        return redirect('teacher_view')
    else:
        messages.error(request, "Teacher Deleted Successfully, but mail not sent!!")
        return redirect('teacher_view')

@login_required(login_url='index')
def teacher_filterview(request):
    teacher = Teacher.objects.all()
    
    return render(request, 'teacher/teachers_filter.html', {'teachers':teacher})

# Error Handling

def some_error(request,*args, **argv):
    return render(request,'404.html')


# Student Views
@login_required(login_url='index')
def student_add(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        class_academic = request.POST['class_academic']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        subject3 = request.POST['subject3']
        subject4 = request.POST['subject4']

        mark1 = request.POST['mark1']
        mark2 = request.POST['mark2']
        mark3 = request.POST['mark3']
        mark4 = request.POST['mark4']

        subjects_list = str({subject1:mark1, subject2:mark2, subject3:mark3, subject4:mark4})


        try:
            student = Student.objects.create(
                full_name=full_name,
                age=age,
                date_of_birth=date_of_birth,
                class_academic=class_academic,
                email=email,
                phone_number=phone_number,
                subjects_list=subjects_list
            )
            student.save()
            student_id = Student.objects.get(email=email).id
        except:
            messages.error(request, "Something Wrong with Database!! Please Try Again Later")
            return redirect('student_add')
        
        messages.success(request, "Student added successfully!")
        return redirect('student_view')

    return render(request, 'student/student_add.html')

@login_required(login_url='index')
def student_view(request):
    students = Student.objects.all()

    for student in students:
        subjects_list = eval(student.subjects_list)
        total_marks = 0
        for mark in subjects_list.values():
            total_marks += int(mark)
        student.average = total_marks/len(subjects_list)
            
    # if not students:
    #     messages.error(request,"No Students Added Yet!!")
    #     return redirect("student_view")
    return render(request, 'student/student_view.html', {"students":students})

@login_required(login_url='index')
def student_edit(request, id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        class_academic = request.POST['class_academic']
        phone_number = request.POST['phone_number']
        
        maths = request.POST['maths']
        english = request.POST['english']
        sst = request.POST['sst']

        subjects_list = str({"maths":maths, "english":english, "sst":sst})

        try:
            student = Student.objects.get(id=id)
            student.full_name = full_name
            student.age = age
            student.date_of_birth = date_of_birth
            student.class_academic = class_academic
            student.phone_number = phone_number
            student.subjects_list = subjects_list
            student.save()
            messages.success(request, "Student Updated Successfully!")
            return redirect('student_view')
        except:
            messages.error(request, "Something Wrong with Database!! Please Try Again Later")
            return redirect('student_view')
    
    student = Student.objects.get(id=id)
    subject_list = eval(student.subjects_list)
    return render(request, 'student/student_edit.html',{'student':student, 'subject_list':subject_list})

@login_required(login_url='index')
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student Deleted Successfully!")
    return redirect('student_view')