from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

topics=[
    'difference between Probation vs parole',
    'Learn how to fold shirts so their ironing last',
    'difference between Object oriented Programming vs functional programming'
    ,'The difference between Presidential democracy and Parlimentary democracy',
    'Learn the most underated and useful html tags',
    'Learn 5 Apis that you must use in your next project',
    'Learn the 20 most used idioms according to Stackoverflow',
    'Learn to differentiate the usecase of To and For',
    'Learn to use powerful ways to express yourself and present a positive outlook',
    "Words to Replace 'I Mean...' for Smoother Conversations"

]

seed_data = [
    {
        "Likes": 100,
        "comments": 25,
        "date": "2023-10-13",
        "title": "Probation vs. Parole: A Comprehensive Guide",
        "text": "A detailed analysis of the differences between probation and parole, including their purposes, eligibility criteria, and conditions.",
        "category": "technology"
    },
    {
        "Likes": 50,
        "comments": 10,
        "date": "2023-10-12",
        "title": "Master the Art of Shirt Folding",
        "text": "Learn effective techniques to fold shirts so they stay wrinkle-free for longer.",
        "category": "lifehacks"
    },
    {
        "Likes": 200,
        "comments": 35,
        "date": "2023-10-11",
        "title": "OOP vs. Functional Programming: A Comparative Analysis",
        "text": "Explore the key differences between object-oriented programming and functional programming paradigms.",
        "category": "technology"
    },
    {
        "Likes": 75,
        "comments": 15,
        "date": "2023-10-10",
        "title": "Understanding Presidential vs. Parliamentary Democracy",
        "text": "Compare and contrast the structures, powers, and advantages of these two forms of government.",
        "category": "government"
    },
    {
        "Likes": 150,
        "comments": 30,
        "date": "2023-10-09",
        "title": "Essential HTML Tags for Web Development",
        "text": "Discover the most commonly used HTML tags and their applications in creating web pages.",
        "category": "technology"
    },
    # ... more items ...
]


def index(request):
    return render(request,"index.html")

def showAll(request):
    return render(request,"blogGears/showAll.html",{"articles":seed_data})

def postDetail(request,slug):
    return render(request,"blogGears/show_detail.html",{'data':slug})