# Generated by Django 4.1.4 on 2023-02-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Subject'),
        ),
    ]
