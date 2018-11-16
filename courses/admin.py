from django.contrib import admin

from .models import Course, Test, UserCourse

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(UserCourse)
