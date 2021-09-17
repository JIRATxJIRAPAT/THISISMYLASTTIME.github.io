from django.urls import path

from . import views

app_name = "registers"

urlpatterns = [
    path('',views.index,name="index"),
    path('<course_id>',views.CourseInfo,name="CourseInfo"),
    path('<int:flight_id>/book', views.book, name="book"),
]