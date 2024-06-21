from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def basic(request):
    if request.method =="POST":
        data=request.POST
        name=data.get('name')
        age=data.get('age')
        phone=data.get('phone')
        address=data.get('address')

        print(name)
        print(age)
        print(phone)
        print(address)
        register.objects.create(
            name=name,
            age=age,
            phone=phone,
            address=address,
        )
    queryset=register.objects.all()
        
    return render(request ,"register.html",context={"register":queryset} )

def delete_element(request,id):
    
    queryset=register.objects.get(id=id)
    queryset.delete()
    return redirect("/register/" )

def update_element(request,id):
    
    queryset=register.objects.get(id=id)
   
    if request.method =="POST":
        data=request.POST
        name=data.get('name')
        age=data.get('age')
        phone=data.get('phone')
        address=data.get('address')
        
        queryset.name=name
        queryset.age=age
        queryset.phone=phone
        queryset.address=address
        queryset.save()
        return redirect("/register/" )
    return render(request,"update.html",context={"update":queryset} )

def sign_up(request):
    if request.method =="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.object.filter(username=username)
        if user.exist():
            return redirect("/sign_up/")
        user=User.object.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            )
        user.set_passwor(password)
        user.save()
        return redirect("/sign_up/")
    return render(request,"sign_up.html")
def sign_in(request):
     return render(request,"sign_in.html")