from django.shortcuts import render

from .models import Job


def index(request):
    return render(request, 'jobs/index.html')


def search_jobs(request):
    return render(request, 'jobs/jobs.html')


def show_job(request, id):
    return render(request, 'jobs/job.html')