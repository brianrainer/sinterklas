from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Test(models.Model):
    question = models.TextField()
    choiceA = models.CharField(max_length=100)
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100)
    choiceD = models.CharField(max_length=100)
    correctAnswer = models.CharField(max_length=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
