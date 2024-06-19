from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("This is About page")

def course(request, courseid):
    return HttpResponse(courseid)