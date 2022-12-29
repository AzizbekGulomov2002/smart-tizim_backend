from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','name','phone','parent','birth','one_id']
    list_filter = ['added']
    search_fields =  ['name','phone','parent','birth','one_id']
    list_per_page = 10
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and obj.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and obj.user.is_superuser:
            return False
        return True
    def save_model(self, request, obj, form, change):
        print(obj.user.role)
        if obj.user.role == 'MANAGER' or obj.user.role=='DIRECTOR':
            super().save_model(request, obj, form, change)