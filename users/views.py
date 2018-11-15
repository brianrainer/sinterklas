from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import User


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponse(user)
