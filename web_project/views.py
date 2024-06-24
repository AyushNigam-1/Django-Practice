from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    if request.method == 'POST':
        n1 = int(request.POST.get("ipt1"))
        n2 = int(request.POST.get("ipt2"))
        print(n1+n2)
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def course(request, courseid):
    return HttpResponse(courseid)