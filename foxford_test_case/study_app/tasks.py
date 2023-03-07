from datetime import datetime

from celery import shared_task
from django.db.models import Sum, F, DecimalField

from .models import Teacher, Webinar, Salary


@shared_task
def teacher_salary_calculation(*args):
    # считаем зарплаты по всем учителям в текущем месяце
    teachers = Teacher.objects.all()

    for teacher in teachers:
        # учитываем только завершённые
        completed_webinars = teacher.webinars.filter(
            status=Webinar.StatusChoices.FINISHED,
            start_date__gte=datetime.today().replace(day=1)
        ).aggregate(
            total_hours=Sum('hours', output_field=DecimalField())
        )
        salary_amount = completed_webinars['total_hours'] * teacher.hourly_rate

        # сохраняем итоговый результат в инстанс Salary, чтобы потом отдавать в эндпоинте с зарплатами
        salary, _ = Salary.objects.get_or_create(teacher=teacher)
        salary.salary = salary_amount
        salary.hours = completed_webinars['total_hours']
        salary.save()




