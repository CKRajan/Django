from django.shortcuts import render
from .forms import NewUserForm
from .models import User
from UserdetailsApp import models

# Create your views here.

""" def index(request):
    return render(request,'index.html')
 """
def user_input(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')

    return render(request,'UserdetailsApp/user_input.html',{'form_ip':form})


def user_output(request):

    if request.method == "GET":
         username = request.GET.get('username') 
         output=User.objects.all().filter(username=username).values()
         return render(request,'UserdetailsApp/user_output.html',{"output":output})
    else:
        print('ERROR! NAME DOES NOT EXISTS')
    