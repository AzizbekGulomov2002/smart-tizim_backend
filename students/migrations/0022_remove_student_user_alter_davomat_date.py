# Generated by Django 4.1.4 on 2023-02-21 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_alter_davomat_date_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='davomat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 10, 16, 22, 637911)),
        ),
    ]