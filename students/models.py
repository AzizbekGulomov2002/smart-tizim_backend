from django.db import models
from django.utils.translation import gettext_lazy as _
from center.models import User
from courses.models import Groups, Course, ClassRoom

# Create your models here.
class Student(models.Model):
    class Languages(models.TextChoices):
        UZBEK = "uzbek","O'zbekcha"
        ENGLISH = 'english',"English"
        RUSSIAN = 'russian',"Русский"
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("User"),help_text=_("Select User"))
    name = models.CharField(max_length=40,verbose_name=_("Student Name"),help_text=_("Enter Student Name"),null=True,blank=True)
    phone = models.CharField(max_length=15,unique=True,verbose_name=_("Student Phone Number"),help_text=_("Enter Student Phone Number"),null=True,blank=True)
    parent = models.CharField(max_length=15,verbose_name=_("Parent Phone Number"),help_text=_("Enter Parent Phone Number"),null=True,blank=True)
    birth = models.DateField(verbose_name=_("Student Birth Year"),help_text=_("Enter Student Birth Year"),null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=15,choices=Languages.choices,verbose_name=_("Language"),help_text=_("Enter language"),null=True,blank=True)
    groups = models.ForeignKey(Groups,on_delete=models.CASCADE,null=True,blank=True)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE,null=True,blank=True)
    course =models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=100,help_text=_("Enter address"),verbose_name=_("Address"),null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    one_id = models.CharField(max_length=40,null=True,blank=True)
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        if  not self.one_id:
            self.one_id = self.id +10000
        super(Student, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Students'
        verbose_name = _("Student ")
        verbose_name_plural = _("Students ")
        
        