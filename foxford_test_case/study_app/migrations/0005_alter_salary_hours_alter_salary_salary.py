# Generated by Django 4.1.5 on 2023-03-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0004_remove_salary_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
