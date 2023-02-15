# Generated by Django 4.1.4 on 2023-02-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_alter_davomat_date'),
        ('courses', '0014_groups_finish_lesson_groups_start_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(related_name='classes', to='students.student'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='student',
            field=models.ManyToManyField(related_name='groups', to='students.student'),
        ),
    ]