# Generated by Django 4.1.4 on 2023-01-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_groups_student_groups_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='course',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='room',
        ),
        migrations.AddField(
            model_name='groups',
            name='course',
            field=models.ManyToManyField(to='courses.course'),
        ),
        migrations.AddField(
            model_name='groups',
            name='room',
            field=models.ManyToManyField(to='courses.room'),
        ),
    ]
