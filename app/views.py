from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *


def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            sid=SFD.cleaned_data['sid']
            name=SFD.cleaned_data['name']
            email=SFD.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,name=name,email=email)[0]
            SO.save()
            

        SQS=Student.objects.all()
        d1={'SQS':SQS}
        return render(request,'display_student.html',d1)

    return render(request,'insert_student.html',d)