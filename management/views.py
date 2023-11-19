from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from database.models import *
from utilities.functions import send_email

def index(request):
    messages.info(request, "Hello world!")
    return render(request, 'index.html')

# Teacher Views
def teacher_dashboard(request):
    return render(request, 'teacher/dashboard.html')

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
            return redirect('teacher_add')
        else:
            messages.error(request, f"Mail Not Sent, but teacher created with ID: {teacher_id} ")
    return render(request, 'index.html')

def teacher_view(request):
    teachers = Teacher.objects.all()
    if not teachers:
        messages.error(request,"No Teachers Added Yet!!")
        return redirect("teacher_view")
    return render(request, 'teacher/teachers_view.html', {"teachers":teachers})