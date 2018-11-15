from django.conf import settings
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.user, self.job)


class Employment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return '{}, {}'.format(self.user, self.job)
