from django.shortcuts import render,redirect
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

def update_teacher(request,id):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")

        teacher = Teacher(
            id = id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("all-teachers")
    return render(request,"index.html",{'teacher':teacher})