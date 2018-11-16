from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Job


def index(request):
    return render(request, 'jobs/index.html')


def search_jobs(request):
    keyword = request.GET.get('keyword')
    location = request.GET.get('location')
    jobs = Job.objects.filter(title__icontains=keyword, location__icontains=location, is_taken=False)

    return render(request, 'jobs/jobs.html', {
        'keyword': keyword,
        'location': location,
        'jobs': jobs,
    })


def show_job(request, id):
    job = get_object_or_404(Job, id=id)

    return render(request, 'jobs/job.html', {'job': job})
