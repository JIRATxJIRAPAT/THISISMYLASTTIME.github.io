
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from .models import Course,Student

def CourseList(request):
    return render(request,"registers/index.html",{
        "courselist": Course.objects.all()
    })


def CourseInfo(request,course_id):
    info = get_object_or_404(Course,pk=course_id)
    return render(request,"registers/course_info.html",{
        "info": info,
        "student":info.enroll.all(),
        "non_enrollment": Student.objects.exclude(enroll=info)
    })


def book(request, course_id):
    if request.method == "POST":
        info = get_object_or_404(Course,pk=course_id)
        student = request.POST["enroll"]
        info.enroll.add(student)
        return HttpResponseRedirect(reverse("registers:CourseInfo", args=(course_id,))
        ) 
    
    