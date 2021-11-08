from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    dept = models.CharField(max_length=250)

    def __str__(self):
        return self.dept

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studname=models.CharField(max_length=250)
    dept = models.ForeignKey(Department,related_name="student_dept",on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.studname

    class Meta:
        ordering = ['roll_no']

class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name 

class LecturerInDept(models.Model):
    department = models.ForeignKey(Department,related_name="department",on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer,related_name="lect_dept",on_delete=models.CASCADE)

    def __str__(self):
        return self.lecturer.name

    class Meta:
        unique_together = ('department','lecturer')              