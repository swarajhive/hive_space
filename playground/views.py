from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return render(request,"hello.html")
# Create your views here.
