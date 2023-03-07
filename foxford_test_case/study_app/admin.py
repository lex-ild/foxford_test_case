from django.contrib import admin

from .models import Teacher, Course, Webinar, Salary

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Webinar)
admin.site.register(Salary)
