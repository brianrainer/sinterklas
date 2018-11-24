from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from jobs.models import Job, Employment, Application

from .models import User


def profile(request, username):
    user = get_object_or_404(User, username=username)
    employments = Employment.objects.filter(application__user__username=username, is_done=True)

    return render(request, 'users/profile.html', {
        'user': user,
        'employments': employments
    })


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('/dashboard/')
        except:
            messages.error(request, 'Username/password salah.')
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            auth_login(request, user)
            return HttpResponseRedirect('/dashboard/')
        except:
            messages.error(request, 'Username/email sudah terpakai.')
            return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')


@login_required(login_url='/login/')
def dashboard(request):
    jobs = Job.objects.filter(user=request.user)
    applications = Application.objects.filter(user=request.user)
    employments = Employment.objects.filter(application__user=request.user)

    return render(request, 'users/dashboard.html', {
        'jobs': jobs,
        'applications': applications,
        'employments': employments,
    })


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
