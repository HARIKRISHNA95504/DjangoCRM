from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.student_list, name='all-students'),
    path('add-studetnt/', views.add_student, name="addstudent"),
    #  path("updatestudent/<str:id>", views.update_student, name="updatestudent"),
    path('update-student/<str:id>',views.update_student,name="update-student"),
    path('delete-student/<str:id>',views.delete_student,name="delete-student")

]