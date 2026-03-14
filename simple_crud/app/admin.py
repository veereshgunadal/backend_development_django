from django.contrib import admin
from app.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','roll','name','branch']

admin.site.register(Student, StudentAdmin)