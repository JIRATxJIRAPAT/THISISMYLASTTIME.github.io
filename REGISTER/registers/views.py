
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from .models import Course,Student

def index(request):
    return render(request,"registers/index.html",{
        "courselist": Course.objects.all()
    })


def CourseInfo(request,course_id):
    info = get_object_or_404(Course,pk=course_id)
    return render(request,"registers/course_info.html",{
        "Course": info,
        "student":info.enroll.all(),
        #"non_enrollment": Student.objects.exclude(enrollment=info)
    })



    
    