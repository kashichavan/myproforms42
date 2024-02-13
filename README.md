Inserting data from the forms to database:
----------------------------------------

if we want to insert data than we must go to view of the form

Step 1): first check whether the request.method is POST or not

	if request.method=="POST":

Step 2): if it is post then we need to create object for the formClass
	by passing taken data to the class in way of request.POST

	request.POST--> it is QueryDict variable which carries all the data 
	sent from the form.

	form=EmployeeForm(request.POST)

Step 3): check whether the form object is valid or not by using is_valid()
		 if form.is_valid():

step 4) if it is valid then get each field from request.POST[fieldName]

	    ename=request.POST['name']
            eage=request.POST['age']
            edesignation=request.POST['designation']
            eEmail=request.POST['email']
            eSal=request.POST['sal']
Step 5) By using django orm concept store the data into data base

EmployeeModel.objects.create(name=ename,age=eage,designation=edesignation,email=eEmail,sal=eSal)



Complete code :
--------------
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
 
