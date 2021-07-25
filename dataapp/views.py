from django.shortcuts import render
from .forms import *

from .models import *


# Create your views here.
def index(request):
    data = Student.objects.all()
    
    
    
    dict = {'student':data}        
    return render(request,'index.html',context=dict)


def details(request,id):
    data = Student.objects.get(id = id)
    dict = {"info":data}
    return render(request,'details.html',context=dict)

def form(request):
   
    form = StudentForn()
    if request.method =="POST":
        form = StudentForn(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    dict = {"forms":form}

    return render(request,'form.html',context=dict)

def update(request,id):
    data = Student.objects.get(id=id)
   
    form = StudentForn(instance=data)
    if request.method=="POST":
        form = StudentForn(request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    dict = {'form':form}
    return render(request,'update.html',context=dict)
   
    



def delete(request,id):
    data = Student.objects.get(id=id).delete()
    dict = {'msg':'Yor Info Has been edeleted'}
    return render(request,'delete.html',context=dict)

