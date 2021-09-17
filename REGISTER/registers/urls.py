from django.urls import path

from . import views

app_name = "registers"

urlpatterns = [
    path('',views.index,name="index"),
    path('<course_id>',views.CourseInfo,name="CourseInfo")
]