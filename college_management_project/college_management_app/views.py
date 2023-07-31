from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import CustomUser, Staffs, Students, AdminHOD

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def loginUser(request):
    return render(request, 'login_page.html')

def doLogin(request):
    print('Here')
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    # user_type = request.GET.get('user_type')
    # print(email_id)
    # print(password)
    if not (email_id and password):
        messages.error(request, 'please provide the all details')
        return render(request, 'login_page.html')
    user = CustomUser.objects.filter(email=email_id, password=password)

    if not user:
        messages.error(request, 'Invalid credentials')
        return render(request, 'login_page.html')
    login(request, user)


    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type == CustomUser.HOD:
        return render(request, 'admin_home.html')
    
    return render(request, 'home.html')


def registration(request):
    return render(request, 'registration.html')

def doRegistration(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    confirm_password = request.GET.get('confirmPassword')

    if not (email_id and password and confirm_password):
        messages.error(request, 'Please provide the all detail')
        return render(request, 'registration.html')
    
    if password != confirm_password:
        messages.error(request, 'Both passwords should match')
        return render(request, 'registration.html')
    is_user_exists = CustomUser.objects.filter(email=email_id).exists

    if is_user_exists:
        messages.error(request, 'User with the email alreday exists,, please login')
        return render(request, 'registration.html')
    user_type = get_user_type_from_email(email_id)
    
    if user_type is None:
        messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
        return render(request, 'registration.html')
    
    
    username = email_id.split('@')[0].split('.')[0]
    if CustomUser.objects.filter(username=username).exists():
        messages.error(request, 'User with this username already exists. Please use different username')
        return render(request, 'registration.html')
    
    user = CustomUser()
    user.username = username
    user.email = email_id
    user.password = password
    user.user_type = user_type
    user.first_name = first_name
    user.last_name = last_name
    user.save()



    
    if user_type == CustomUser.STAFF:
        Staffs.objects.create(admin=user)
    elif user_type == CustomUser.STUDENT:
        Students.objects.create(admin=user)
    elif user_type == CustomUser.HOD:
        AdminHOD.objects.create(admin=user)
    return render(request, 'login_page.html')



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def get_user_type_from_email(email_id):
        """
        Returns CustomUser.user_type corresponding to the given email address
        email_id should be in following format:
        '<username>.<staff|student|hod>@<college_domain>'
        eg.: 'abhishek.staff@jecrc.com'
        """

        try:
            email_id = email_id.split('@')[0]
            email_user_type = email_id.split('.')[1]
            return CustomUser.EMAIL_TO_USER_TYPE_MAP(email_user_type)
        except:
            return None


 

















    



