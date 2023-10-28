from django.shortcuts import render, redirect
from .models import Employee


# Create your views here.
def home(request):
    listEmployee = Employee.objects.all
    return render(request, 'home.html', {'employees':listEmployee})

def insertEmployee(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']

    employee = Employee.objects.create(code=code, name=name)
    return redirect('/')

def editEmployee(request, code):
    if request.method == 'GET':
        employee = Employee.objects.get(code=code)
        return render(request, "editEmployee.html", {"employee": employee})

    elif request.method == 'POST':
        name = request.POST.get('txtName')
        employee = Employee.objects.get(code=code)
        employee.name = name
        employee.save()
        return redirect('/')
def deleteEmployee(request, code):
    employee = Employee.objects.get(code=code)
    employee.delete();
    return redirect('/')

