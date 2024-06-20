from django.shortcuts import render,redirect
from .models import *
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