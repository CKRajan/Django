from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from collegeinfo.models import Department,Student,Lecturer,LecturerInDept

# Create your views here.
def search_dept(request):
    query = request.GET.get("dept", None)
    depart = Department.objects.filter(dept=query)
    dept_id=0
    for y in depart:
        dept_id=y.id
    students = Student.objects.filter(dept=dept_id)

    lect=LecturerInDept.objects.filter(department=dept_id)
    lect_id=[]
    lect_name=[]
    for y in lect:
        lect_id.append(y.lecturer)
    for x in lect_id:
        lect_name.append(x)
        
    context = {
        "department": depart,
        "student": students,
        "lecturer_list":lect_name,
    }
    template = "collegeinfo/search_dept.html"
    return render(request, template, context)

def search_student(request):
    query = request.GET.get("stud", None)
    students = Student.objects.filter(studname=query)
    dept_id=0
    for y in students:
        dept_id=y.dept_id
    deptname = Department.objects.filter(id=dept_id)
    context = {
        "stud_details": students,
        "department": deptname,
    }
    template = "collegeinfo/search_student.html"
    return render(request, template, context)

def search_faculty(request):
    query = request.GET.get("lect", None)
    lect = Lecturer.objects.filter(name=query)

    lect_id=0
    for y in lect:
        lect_id=y.id
    lect=LecturerInDept.objects.filter(lecturer=lect_id)
    dep_id=[]
    deptname=[]
    for x in lect:
        dep_id.append(x.department)
    for y in dep_id:
        deptname.append(y)
       
    context = {
        "lecturer": query,
        "department":deptname,
    }
    template = "collegeinfo/search_faculty.html"
    return render(request, template, context)   