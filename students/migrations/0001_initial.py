# Generated by Django 4.1.4 on 2022-12-26 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter Student Name', max_length=40, null=True, verbose_name='Student Name')),
                ('phone', models.CharField(blank=True, help_text='Enter Student Phone Number', max_length=15, null=True, unique=True, verbose_name='Student Phone Number')),
                ('parent', models.CharField(blank=True, help_text='Enter Parent Phone Number', max_length=15, null=True, verbose_name='Parent Phone Number')),
                ('birth', models.DateField(blank=True, help_text='Enter Student Birth Year', null=True, verbose_name='Student Birth Year')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(blank=True, choices=[('uzbek', "O'zbekcha"), ('english', 'English'), ('russian', 'Русский')], help_text='Enter language', max_length=15, null=True, verbose_name='Language')),
                ('address', models.CharField(blank=True, help_text='Enter address', max_length=100, null=True, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('one_id', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.ForeignKey(help_text='Select User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Student ',
                'verbose_name_plural': 'Students ',
                'db_table': 'Students',
            },
        ),
    ]
