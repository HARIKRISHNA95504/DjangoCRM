from django.shortcuts import render,redirect,get_object_or_404

from .models import Student
from django.contrib import messages

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, "students.html", {"allstudents":students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        student = Student(
            name = name,
            age = age,
            contact = contact,
            email = email,
            address = address,
            image = image if image else None
        )
        student.save()
        return redirect("all-students")
    return render(request, "index.html")

def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        # Check if another student already uses the email
        if Student.objects.filter(email=email).exclude(id=id).exists():
            messages.error(request, "Email already exists for another student.")
            return redirect("all-students")

        # updated Existing Student
        student.name = name
        student.age = age
        student.contact = contact
        student.email = email
        student.address = address
        if image:
            student.image = image  # update image only if uploaded
        student.save()
        return redirect("all-students")

    return render(request, "index.html", {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("all-students")
