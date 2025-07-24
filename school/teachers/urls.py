from django.urls import path
from . import views

urlpatterns = [
    path('',views.teacher_list, name='all-teachers'),
    path('add-teacher/',views.add_teacher,name="addteacher")
]