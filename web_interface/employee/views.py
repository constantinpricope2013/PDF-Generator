from django.shortcuts import render
from .forms import EmployeeRegisterForm, EmployeeUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Angajat adaugat cu success!')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'employee/register-employee.html', {'form': form})

@login_required
def view_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Angajat adaugat cu success!')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'employee/register-employee.html', {'form': form})


@login_required
def delete_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Angajat adaugat cu success!')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'employee/register-employee.html', {'form': form})

@login_required
def update_employee(request):
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Datele angajatului actualizate cu success!')
            return redirect('employee-home.html')
    else:
        form = EmployeeUpdateForm()
    return render(request, 'employee/update-employee.html', {'form': form})

@login_required
def employee_home(request):
    return render(request, 'employee/employee-home.html')