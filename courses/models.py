from django.db import models
from students.models import Student
# Create your models here.
from django.utils.translation import gettext_lazy as _ 
class Course(models.Model):
    name = models.CharField(max_length=100,help_text=_("Enter course name"),verbose_name=_("Course name"))
    cost = models.CharField(max_length=600,verbose_name=_("Cost"),help_text=_("Enter cost"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Courses"
        verbose_name = " Course "
        verbose_name_plural = " Courses "
    
class Room(models.Model):
    name = models.CharField(max_length=500,verbose_name=_("Room name"))
    student_count = models.IntegerField(verbose_name=_("Students Count"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Rooms"
        verbose_name = " Room "
        verbose_name_plural = " Rooms "
    
class Groups(models.Model):
    class Education(models.TextChoices):
        ONLINE = 'online','Online'
        OFFLINE = 'offline','Offline'
    class Status(models.TextChoices):
        ACTIVE = 'active','Active'
        WAITING = 'waiting','Waiting'
    name = models.CharField(max_length=100,verbose_name=_("Group name"))
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=_("Course"))
    education = models.CharField(max_length=10,choices=Education.choices)
    status = models.CharField(max_length=10,choices=Status.choices)
    start = models.DateField(null=True,blank=True)
    finish = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Groups"
        verbose_name = " Group "
        verbose_name_plural = " Groups "
    
    