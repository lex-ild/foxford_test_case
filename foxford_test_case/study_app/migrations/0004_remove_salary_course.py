# Generated by Django 4.1.5 on 2023-03-06 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0003_alter_webinar_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='course',
        ),
    ]
