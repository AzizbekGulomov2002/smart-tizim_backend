from django.db import models
from students.models import Student
# Create your models here.
from center.models import User
class StudentPayment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True,related_name='payment')
    payment_type = (
        ('naqd',"Naqd"),
        ('plastik karta','Plastik karta'),
        ('click','Click'),
        ('boshqa','Boshqa')
    )
    cost = models.CharField(max_length=1000,null=True,blank=True)
    type = models.CharField(max_length=55,choices=payment_type,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.name} {self.cost} to'lov qildi!"


