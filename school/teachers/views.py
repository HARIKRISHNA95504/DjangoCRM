from django.shortcuts import render,redirect,get_object_or_404
from .models import Teacher
# Create your views here.

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "index.html",{"allteachers":teachers})

# to add the teacher
def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")

        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save() 
        return redirect("all-teachers")
    return render(request,"index.html")

def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image") 

        # Check if another teacher already uses the same email
        if Teacher.objects.filter(email=email).exclude(id=id).exists():
            messages.error(request, "Email already exists for another teacher.")
            return redirect("all-teachers")

        # Update teacher fields
        teacher.name = name
        teacher.subject = subject
        teacher.contact = contact
        teacher.email = email
        if image:
            teacher.image = image

        teacher.save()
        return redirect("all-teachers")

    return render(request, "index.html", {"teacher": teacher})

def delete_teacher(request,id):
    teacher = Teacher.objects.filter(id=id)
    teacher.delete()

    return redirect("all-teachers")