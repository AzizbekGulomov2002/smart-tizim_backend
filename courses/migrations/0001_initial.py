# Generated by Django 4.1.4 on 2023-01-11 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ClassRoom name')),
            ],
            options={
                'db_table': 'ClassRoom',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter course name', max_length=100, verbose_name='Course name')),
                ('cost', models.CharField(help_text='Enter cost', max_length=600, verbose_name='Cost')),
            ],
            options={
                'verbose_name': ' Course ',
                'verbose_name_plural': ' Courses ',
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Room name')),
                ('student_count', models.IntegerField(verbose_name='Students Count')),
            ],
            options={
                'verbose_name': ' Room ',
                'verbose_name_plural': ' Rooms ',
                'db_table': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Group name')),
                ('education', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('waiting', 'Waiting')], max_length=10)),
                ('start', models.DateField(blank=True, null=True)),
                ('finish', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.room')),
                ('student', models.ManyToManyField(to='students.student')),
            ],
            options={
                'verbose_name': ' Group ',
                'verbose_name_plural': ' Groups ',
                'db_table': 'Groups',
            },
        ),
    ]
