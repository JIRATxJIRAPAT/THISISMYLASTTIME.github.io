from django.contrib import admin
from .models import Course,Student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    filter_horizontal = ("enroll",)

admin.site.register(Course)
admin.site.register(Student,studentAdmin)