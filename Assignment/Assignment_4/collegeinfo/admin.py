from django.contrib import admin

from .models import Student,Department,Lecturer,LecturerInDept
# Register your models here.

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Department)
admin.site.register(LecturerInDept)