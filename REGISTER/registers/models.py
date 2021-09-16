from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=5 , primary_key= True)
    course_name = models.CharField(max_length=64)
    semester = models.PositiveIntegerField()
    limit_seat = models.PositiveIntegerField()
    academic_year = models.PositiveIntegerField()
    status = models.BooleanField()
    
    def __str__(self) -> str:
         return f"{self.course_id} ({self.course_name})"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enroll = models.ManyToManyField(Course, blank=True, related_name="enroll")
    

    def __str__(self) -> str:
         return f"{self.user} " 