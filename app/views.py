from django.shortcuts import render
from app import models , forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout 
from sendsms import api
from django.http import HttpResponseRedirect




def home(request):
    context={}
    return render(request,'home.html',context)




def registration(request):
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
        if query:
            candidate = User.objects.create_user(username=email,password=password)
            query.save()
            x=True
            context={
                'x':x
            }
            return render(request,'login.html',context)
    return render(request,'registration.html')




def patient(request):
    queryset = models.DetailsOfDoctors.objects.all()
    context={
        'x':queryset
    }
    print(queryset)
    return render(request,'patient.html',context)




def LogIn(request):
    context={}
    if request.method == "POST":
        username = request.POST.get('email_name')
        password = request.POST.get('password_name')
        x = authenticate(username=username,password=password)
        if x:
            login(request,x)
            details = models.PatientDetails.objects.all()
            context = {
                'details':details
            }
            return render(request,'view.html',context)
        else:
            pass
    return render(request,'login.html',context)




@login_required(login_url='/login')
def DoctorView(request):
    context={}
    return render(request,'view.html',context)




def detail(request,pk):
    query = models.DetailsOfDoctors.objects.get(pk=pk)
    form = forms.Patient()
    if request.method == "POST":
        form = forms.Patient(request.POST)
        name = request.POST['Name']
        if form.is_valid():
            form.save()
            x=True
            context={
                'x':x,
                'name':name
            }
            return render(request,'home.html',context)
    context={
        'query':query,
        'form':form
    }
    return render(request,'detail.html',context)




def LogOut(request):
    logout(request)
    y=True
    context={
        'y':y
    }
    return render(request,'home.html',context)




def about(request):
    return render(request,'about.html')



def sms(request):
    api.send_sms(body='I can haz txt', from_phone='+919667626421', to=['+919560440822'])
    return HttpResponseRedirect('/home')