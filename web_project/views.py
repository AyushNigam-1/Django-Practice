from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import usersForm
def homepage(request):
    url=""
    fo = usersForm()
    data = {
    "output":fo    
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
        output = request.GET.get("ipt1")
        
    url = "/about?output={}".format(output)
    return redirect(url)