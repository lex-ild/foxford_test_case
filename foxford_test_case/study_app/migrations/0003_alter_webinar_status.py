# Generated by Django 4.1.7 on 2023-03-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0002_salary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Live', 'Live'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], max_length=10),
        ),
    ]
