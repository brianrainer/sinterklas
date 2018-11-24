from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import utc
import datetime

from .models import Job, Application, Employment


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
    applications = Application.objects.filter(job=job)
    isOwner = False
    hasApplication = False

    if request.user.is_authenticated:
        if job.user == request.user:
            isOwner = True
        try:
            Application.objects.get(user=request.user, job=job)
            hasApplication = True
        except:
            pass

    try:
        employment = Employment.objects.get(application__job=job)
    except:
        employment = None

    return render(request, 'jobs/job.html', {
        'job': job,
        'applications': applications,
        'isOwner': isOwner,
        'hasApplication': hasApplication,
        'employment': employment,
    })


def create_job(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        job = Job.objects.create(title=title, description=description, location=location, user=request.user)
        messages.success(request, 'Pekerjaan berhasil dibuat.')
        return HttpResponseRedirect('/jobs/{}'.format(job.id))
    
    return HttpResponseRedirect('/')


def apply_job(request):
    if request.method == 'POST' and request.user.is_authenticated:
        id = request.POST['id']
        job = get_object_or_404(Job, id=id)
        job.save()
        Application.objects.create(user=request.user, job=job)
        messages.success(request, 'Lamaran berhasil dikirimkan.')
        return HttpResponseRedirect('/jobs/{}'.format(id))
    
    return HttpResponseRedirect('/')


def accept_application(request):
    if request.method == 'POST':
        id = request.POST['id']
        application = get_object_or_404(Application, id=id)

        if request.user == application.job.user:
            application.is_accepted = True
            application.save()
            application.job.is_taken = True
            application.job.save()
            Employment.objects.create(application=application)
            messages.success(request, 'Lamaran berhasil diterima.')
            return HttpResponseRedirect('/jobs/{}'.format(application.job.id))
    
    return HttpResponseRedirect('/')


def finish_employment(request):
    if request.method == 'POST':
        id = request.POST['id']
        rating = request.POST['rating']
        review = request.POST['review']
        employment = get_object_or_404(Employment, id=id)

        if request.user == employment.application.job.user:
            employment.is_done = True
            employment.date_ended = datetime.datetime.utcnow().replace(tzinfo=utc) 
            employment.rating = rating
            employment.review = review
            employment.save()
            messages.success(request, 'Pekerjaan teleh diselesaikan.')
            return HttpResponseRedirect('/jobs/{}'.format(employment.application.job.id))
    
    return HttpResponseRedirect('/')
