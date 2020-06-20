from django.shortcuts import render
from app import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    context={}
    return render(request,'home.html',context)


def registration(request):
    x = False
    query = None
    context={}
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('AddressName')
        city = request.POST.get('city_name')
        state = request.POST.get('state_name')
        email = request.POST.get('email_name')
        number = request.POST.get('contact_name')
        image = request.POST.get('image')
        password = request.POST.get('password_name')
        query = models.DetailsOfDoctors(name=name,address=address,city=city,state=state,email=email,number=number,image=image)
        query.save()
        if query:
            x = True
            candidate = User.objects.create_user(username=email,password=password)
            context={
                'x':x
            }
    return render(request,'registration.html',context)


def patient(request):
    queryset = models.DetailsOfDoctors.objects.all()
    context={
        'x':queryset
    }
    print(queryset)
    return render(request,'patient.html',context)


@login_required()
def LogIn(request):
    context={}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST('')
        x = authenticate(username=username,password=password)
        if x:
            return HttpResponseRedirect('/')
        else:
            context={
                'x':x
            }
    return render(request,'login.html',context)
