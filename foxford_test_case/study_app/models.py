from django.db import models
from django.db.models import TextChoices


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Webinar(models.Model):
    class StatusChoices(TextChoices):
        CREATED = 'Created'
        LIVE = 'Live'
        FINISHED = 'Finished'
        CANCELLED = 'Cancelled'

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    teachers = models.ManyToManyField(Teacher, related_name='webinars')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hours = models.FloatField(null=True, blank=True)

    # переопределяем init, чтобы сразу считать часы по времени начала и окончания вебинара
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hours = self.end_date.hour - self.start_date.hour


class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
