from django.urls import path
from collegeinfo import views

app_name = 'collegeinfo'

urlpatterns =[
   path('search_dept/',views.search_dept,name="search_dept"),
   path('search_student/',views.search_student,name="search_student"),
   path('search_faculty/',views.search_faculty,name="search_faculty"),
]
