from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    data={
        "title":"Love",
        "list":["Ayush","Ayush","Ayush"]
    }
    return render(request,"index.html",data)

def about(request):
    return HttpResponse("This is About page")

def course(request, courseid):
    return HttpResponse(courseid)