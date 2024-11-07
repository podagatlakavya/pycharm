from django.contrib import admin
from StudentDB1App.models import Student
#Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
admin.site.register(Student,StudentAdmin);

class Student2Admin(admin.ModelAdmin):
    list_display=['rollno', 'name', 'dob','marks','email', 'phonenumber','address']
admin.site.register(Student,Student2Admin);
