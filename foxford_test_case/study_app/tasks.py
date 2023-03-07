from datetime import datetime

from django.db.models import Sum, FloatField, F

from foxford_test_case.celery import app
from .models import Teacher, Webinar, Salary


@app.task()
def teacher_salary_calculation(*args):
    # считаем зарплаты по всем учителям в текущем месяце
    teachers = Teacher.objects.all()

    for teacher in teachers:
        # учитываем только завершённые
        completed_webinars = Webinar.objects.filter(
            status=Webinar.StatusChoices.FINISHED,
            teachers=teacher,
            start_date__gte=datetime.today().replace(day=1)
        ).aggregate(
            webinars_salary=teacher.hourly_rate * Sum('hours'),
            hours=Sum('hours'),
        )

        # сохраняем итоговый результат в инстанс Salary, чтобы потом отдавать в эндпоинте с зарплатами
        try:
            salary = Salary.objects.get(teacher=teacher)
            salary.salary = completed_webinars['webinars_salary']
            salary.hours = completed_webinars['hours']
            salary.save()

        except Salary.DoesNotExist:
            salary = Salary.objects.create(
                salary=completed_webinars['webinars_salary'],
                hours=completed_webinars['hours'],
                teacher=teacher
            )
            salary.save()




