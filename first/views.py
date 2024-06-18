from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people=[{'name':'yash','age':'21'},
            {'name':'harsh','age':'20'},
            {'name':'yc','age':'25'},]
    
    return render(request ,"home.html",context={"data":people})
def basic(request):
    return render(request ,"basic.html" )
