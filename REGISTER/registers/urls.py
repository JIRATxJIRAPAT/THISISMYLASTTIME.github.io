from django.urls import path

from . import views

app_name = "registers"

urlpatterns = [
    path('',views.CourseList,name="index"),
    path('<course_id>',views.CourseInfo,name="CourseInfo"),
    path('<course_id>/enroll', views.book, name="book"),
]