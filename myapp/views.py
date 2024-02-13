from django.shortcuts import render
from .forms import EmployeeForm
from .models import EmployeeModel

# Create your views here.
def  register(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            ename=request.POST['name']
            eage=request.POST['age']
            edesignation=request.POST['designation']
            eEmail=request.POST['email']
            eSal=request.POST['sal']
            EmployeeModel.objects.create(name=ename,age=eage,designation=edesignation,email=eEmail,sal=eSal)


    f=EmployeeForm()        
    return render(request,'register.html',context={'form':f})
