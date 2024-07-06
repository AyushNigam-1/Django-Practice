from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import usersForm
from service.models import Service
from news.models import News
def homepage(request):
    serviceData = Service.objects.all().order_by('-service_title')
    print(serviceData)
    url=""
    fo = usersForm()
    data = {
    "output":serviceData    
    }
    print(data)
    if request.method == 'POST':
        n1 = int(request.POST.get("ipt1"))
        n2 = int(request.POST.get("ipt2"))
        res = n1+n2
        url = "/about?output={}".format(res)
        return HttpResponseRedirect(url)
    return render(request , "index.html" , data)

def about(request):
    if request.method == 'GET':
        output = request.GET.get("output")
    return render(request,"about.html",{"output":output})

def course(request, courseid):
    return HttpResponse(courseid)

def formData(request):
    if request.method == 'GET':
        output = request.GET.get("num1")
        # print ("output --> {}".format(output))
        if(output == "1"):
            return render(request ,"index.html" , {"error":True})
        
    url = "/about?output={}".format(output)
    return redirect(url)

def item(request , slug):
    record = Service.objects.get(slug = slug)
    print(record)
    output = {
        "record":record
    }
    return render(request , "about.html",output)

def item(request , id):
    record = Service.objects.get(id = id)
    record = Service.objects.filter(service_title = id)
    print(record)
    output = {
        "record":record
    }
    return render(request , "about.html",output)

