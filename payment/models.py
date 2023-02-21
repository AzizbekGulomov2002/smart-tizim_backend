from django.db import models
from students.models import Student
from center.models import User
from courses.models import Groups
class StudentPayment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True,related_name='payment')
    group = models.ForeignKey(Groups,on_delete=models.SET_NULL,null=True,blank=True)
    payment_type = (
        ('naqd',"Naqd"),
        ('plastik karta','Plastik karta'),
        ('click','Click'),
        ("pul ko'chirish","Pul ko'chirish"),
        ('boshqa','Boshqa')
    )
    cost = models.CharField(max_length=1000,null=True,blank=True)
    type = models.CharField(max_length=55,choices=payment_type,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.student.name} {self.cost} to'lov qildi!"


