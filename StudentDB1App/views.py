from django.shortcuts import render
from StudentDB1App.models import Student

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')		#def-order is ASC-order (DJ-ORM-code)
    dict1={'studentlist':studentlist}
    return render(request,'StudentDB1App/students.html',context=dict1);