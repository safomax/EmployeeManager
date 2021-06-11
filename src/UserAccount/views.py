from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Employee, Office, Position, Team
from django.contrib.auth.models import User


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'UserAccount/register.html', context)


def createEmployeeAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return redirect('dashboard')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('dashboard')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return render(request, 'UserAccount/dashboard.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                messages.info(request, 'Username or password is incorrect!')

        context = {}
        return render(request, 'UserAccount/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def landing(request):
    context = {}
    return render(request, 'UserAccount/landing.html', context)


@login_required(login_url='login')
def dashboard(request):
    employeeData = Employee.objects.all()
    officeData = Office.objects.all()
    positionData = Position.objects.all()
    teamData = Team.objects.all()

    if request.method == 'POST':
        if request.POST.get('employee_id') and request.POST.get('gender') and request.POST.get(
                'first_name') and request.POST.get('last_name') and request.POST.get(
                'employment_date') and request.POST.get('working_hours_from') and request.POST.get(
                'working_hours_to') and request.POST.get('email') and request.POST.get(
                'primary_address') and request.POST.get('city') and request.POST.get('state') and request.POST.get(
                'postalCode') and request.POST.get('primary_phone_number') and request.POST.get(
                'other_phone_number') and request.POST.get('date_of_birth') and request.POST.get(
                'salary') and request.POST.get('status'):

            print("POST employee")
            employee = Employee()
            employee.employee_id = request.POST.get('employee_id')
            employee.gender = request.POST.get('gender')
            employee.first_name = request.POST.get('first_name')
            employee.last_name = request.POST.get('last_name')
            employee.employment_date = request.POST.get('employment_date')
            employee.working_hours_from = request.POST.get('working_hours_from')
            employee.working_hours_to = request.POST.get('working_hours_to')
            employee.email = request.POST.get('email')
            employee.primary_address = request.POST.get('primary_address')
            employee.city = request.POST.get('city')
            employee.state = request.POST.get('state')
            employee.postalCode = request.POST.get('postalCode')
            employee.primary_phone_number = request.POST.get('primary_phone_number')
            employee.other_phone_number = request.POST.get('other_phone_number')
            employee.date_of_birth = request.POST.get('date_of_birth')
            employee.salary = request.POST.get('salary')
            employee.status = request.POST.get('status')
            employee.save()

            return render(request, "UserAccount/dashboard.html")

        if request.POST.get('office_address') and request.POST.get('city') and request.POST.get(
                'state') and request.POST.get('postalCode'):
            print("POST Office address")
            office = Office()
            office.office_address = request.POST.get('office_address')
            office.city = request.POST.get('city')
            office.state = request.POST.get('state')
            office.postalCode = request.POST.get('postalCode')
            office.save()

            return render(request, 'UserAccount/dashboard.html')

        if request.POST.get('position'):
            print("POST Position")
            position = Position()
            position.position = request.POST.get('position')
            position.save()

            return render(request, 'UserAccount/dashboard.html')

        if request.POST.get('team'):
            print("POST Team")
            team = Team()
            team.team = request.POST.get('team')
            team.save()

            return render(request, 'UserAccount/dashboard.html')

        else:
            return render(request, 'UserAccount/dashboard.html')

    mydict = {"data": employeeData, 'data2': officeData, 'data3': teamData, 'data4': positionData}

    return render(request, 'UserAccount/dashboard.html', context=mydict)
