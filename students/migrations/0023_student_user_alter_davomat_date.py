# Generated by Django 4.1.4 on 2023-02-21 05:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0022_remove_student_user_alter_davomat_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Select User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='davomat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 10, 45, 50, 595007)),
        ),
    ]
