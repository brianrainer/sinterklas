from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.search_jobs, name='jobs'),
    path('jobs/new/', views.create_job, name='create_job'),
    path('jobs/<int:id>', views.show_job, name='job'),
    path('jobs/apply/', views.apply_job, name='apply_job'),
    path('jobs/accept/', views.accept_application, name='accept_application'),
    path('jobs/finish/', views.finish_employment, name='finish_employment'),
]