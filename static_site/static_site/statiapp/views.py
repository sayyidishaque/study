# virtualenv = static
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place
from .models import meet_team


# Create your views here.


def index(request):
    nplace = place.objects.all()
    nteem = meet_team.objects.all()
    return render(request, 'index.html', {'change_place': nplace, 'change_meet': nteem})


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username Already Exist')
                return redirect('static_app:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This Email is already registered')
                return redirect('static_app:registration')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save()
                print('user saved')
                messages.info(request, "User Created")
                return redirect('static_app:login')
        else:
            messages.info(request, 'password & confirm password does not match')
            return redirect('static_app:registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid usename\password')
            return redirect('static_app:login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

# def saveuser(request):
