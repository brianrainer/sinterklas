from django.shortcuts import get_object_or_404, render

from jobs.models import Employment
from .models import User


def profile(request, username):
    user = get_object_or_404(User, username=username)
    employments = Employment.objects.filter(application__user__username=username, is_done=True)

    return render(request, 'users/profile.html', {
        'user': user,
        'employments': employments
    })


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')
