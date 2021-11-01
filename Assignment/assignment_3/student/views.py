from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

# Create your views here.

class StudentList(ListView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'regno', 'id']
    success_url = reverse_lazy('student:student_list')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'regno', 'id']
    success_url = reverse_lazy('student:student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student_list')
