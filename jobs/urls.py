from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.search_jobs, name='jobs'),
    path('jobs/<int:id>', views.show_job, name='job'),
]