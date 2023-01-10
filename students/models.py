from django.db import models
from django.utils.translation import gettext_lazy as _
from center.models import User
from courses.models import Groups, Course, ClassRoom
from django.utils.html import format_html
# Create your models here.
class Student(models.Model):
    class Languages(models.TextChoices):
        UZBEK = "uzbek","O'zbekcha"
        ENGLISH = 'english',"English"
        RUSSIAN = 'russian',"Русский"
    # user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("User"),help_text=_("Select User"))
    name = models.CharField(max_length=40,verbose_name=_("Student Name"),help_text=_("Enter Student Name"),null=True,blank=True)
    phone = models.CharField(max_length=15,unique=True,verbose_name=_("Student Phone Number"),help_text=_("Enter Student Phone Number"),null=True,blank=True)
    parent = models.CharField(max_length=15,verbose_name=_("Parent Phone Number"),help_text=_("Enter Parent Phone Number"),null=True,blank=True)
    birth = models.DateField(verbose_name=_("Student Birth Year"),help_text=_("Enter Student Birth Year"),null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True)
    father_name=models.CharField(max_length=600,null=True,blank=True)
    mother_name = models.CharField(max_length=600, null=True, blank=True)
    language = models.CharField(max_length=15,choices=Languages.choices,verbose_name=_("Language"),help_text=_("Enter language"),null=True,blank=True)
    address = models.CharField(max_length=100,help_text=_("Enter address"),verbose_name=_("Address"),null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Students'
        verbose_name = _("Student ")
        verbose_name_plural = _("Students ")
class Davomat(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='davomat',to_field='phone')
    status = models.BooleanField(default=True)
    date = models.DateTimeField(unique=True)
    description = models.TextField(default="Sabab ko'rsatilmagan")

    def __str__(self):
        return self.student.name
    class Meta:
        verbose_name=" Davomat "
        verbose_name_plural =" Davomatlar "

    @property
    def info(self):
        if self.status:
            return '✅'
        else:
            return '❌'
class Test(models.Model):
    test_kodi = models.CharField(max_length=60)
    fan_nomi = models.CharField(max_length=250)
    talaba = models.CharField(max_length=200)
    telefon_raqam = models.CharField(max_length=40)
    savollar_soni = models.IntegerField()
    togri_javoblar = models.IntegerField()
    def __str__(self):
        return self.test_kodi
    class Meta:
        verbose_name ="Natija "
        verbose_name_plural ="Natijalar "

        
        