from django.contrib import admin
from .models import EmployeeModel

# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['name','age','designation','email','sal']

admin.site.register(EmployeeModel,EmployeeModelAdmin)