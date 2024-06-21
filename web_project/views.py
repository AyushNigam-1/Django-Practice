from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    data={
        "title":"wow",
        "clist":[
            {"name":"Ayush" , "age":"16"},
            {"name":"Ayush","age":"18"},
            {"name":"Ayush","age":"19"}
            ]
    }
    return render(request,"index.html",data)

def about(request):
    return HttpResponse("This is About page")

def course(request, courseid):
    return HttpResponse(courseid)