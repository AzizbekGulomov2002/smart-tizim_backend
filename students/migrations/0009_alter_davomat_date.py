# Generated by Django 4.1.4 on 2023-02-06 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_davomat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davomat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 6, 22, 2, 37, 260398)),
        ),
    ]