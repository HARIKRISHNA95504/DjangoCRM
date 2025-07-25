from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to="students/", blank=True, null=True)
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name}")
