from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return render(request,'one.html')

def add(request):
	num1=int(request.GET['num1'])
	num2=int(request.GET['num2'])
	num3=num1+num2
	ar=[1,3,3,4]
	return render(request,'add.html',{'result': num3,'ar': ar })

def add1(request):
	return render(request,'master.html')