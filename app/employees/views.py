from django.shortcuts import render, redirect


from .models import Employee

from .forms import EmployeeForm
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

def create(request):
    employeeform = EmployeeForm(request.POST)
    if employeeform.is_valid():
        employeeform.save()
        return redirect('employees')
    return render(request, 'employees/create.html', {'employeeform': employeeform})

def edit(request, id):
    employee= Employee.objects.get(id=id)
    employeeform = EmployeeForm(request.POST , instance=employee)
    if employeeform.is_valid() and request.method == 'POST':
        employeeform.save()
        return redirect('employees')
    return render(request, 'employees/edit.html', {'employeeform': employeeform})

def filter_by_name(request):
    if request.GET['name_employee'] != "" and request.GET['card_id'] != "" and request.GET['email'] != "":
        employees= Employee.objects.filter(name_employee=request.GET['name_employee'], card_id=request.GET['card_id'],email=request.GET['email'])
        return render(request, 'employees/index.html', {'employees': employees})
    elif request.GET['name_employee'] != "" and request.GET['card_id'] == "" and request.GET['email'] == "":
        employees= Employee.objects.filter(name_employee=request.GET['name_employee'])
        return render(request, 'employees/index.html', {'employees': employees})
    elif request.GET['name_employee'] == "" and request.GET['card_id'] != "" and request.GET['email'] == "":
        employees= Employee.objects.filter(name_employee=request.GET['card_id'])
        return render(request, 'employees/index.html', {'employees': employees})
    elif request.GET['name_employee'] == "" and request.GET['card_id'] == "" and request.GET['email'] != "":
        employees= Employee.objects.filter(name_employee=request.GET['email'])
        return render(request, 'employees/index.html', {'employees': employees})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employees')


