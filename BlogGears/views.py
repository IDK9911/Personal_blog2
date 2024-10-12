from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

topics=[
    'difference between Probation vs parole',
    'Learn how to fold shirts so their ironing last',
    'difference between Object oriented Programming vs functional programming',
    'The difference between Presidential democracy and Parlimentary democracy',
    'Learn the most underated and useful html tags',
    'Learn 5 Apis that you must use in your next project',
    'Learn the 20 most used idioms according to Stackoverflow',
    'Learn to differentiate the usecase of To and For',
    'Learn to use powerful ways to express yourself and present a positive outlook',
    "Words to Replace 'I Mean...' for Smoother Conversations"

]

def index(request):
    return render(request,"index.html")

def showAll(request):
    return render(request,"blogGears/showAll.html",{"articles":topics})

def postDetail(request,slug):
    return render(request,"blogGears/show_detail.html",{'data':slug})