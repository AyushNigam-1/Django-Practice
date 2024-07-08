from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import usersForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail , EmailMultiAlternatives
def userpage(request):
    print("called" , request.POST.get('icon'))
    if request.method == 'POST':
        icon = request.POST.get('icon')
        title = request.POST.get('title')
        userdetails = Service(service_title = title , service_icon = icon)
        userdetails.save()
    return render(request , 'userForm.html')

def homepage(request):
    send_mail(
        "Testing mail",
        "Here is the message",
        "ayushnigam843@gmail.com",
        ["ayushnigam518@gmail.com"],
        fail_silently=False 
    )
    mail = EmailMultiAlternatives(
        "Testing mail",
        "<h1>Wow bro<h2>",
        "ayushnigam843@gmail.com",
        ["ayushnigam518@gmail.com","ayushnigam35@gmail.com"],
        fail_silently=False 
    )
    mail.content_subtype = "html"
    mail.send()
    serviceData = Service.objects.all().order_by('-service_title')
    paginator = Paginator(serviceData,2)
    page_num = request.GET.get('page')
    final_dt = paginator.get_page(page_num)
    totalpage = final_dt.paginator.num_pages
    print(final_dt)
    url=""
    fo = usersForm()
    data = {
    "output":final_dt ,
    "count":totalpage,
    "pages":[n+1 for n in range(totalpage)]   
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
    # record = Service.objects.filter(service_title = id)
    print(record)
    output = {
        "record":record
    }
    return render(request , "about.html",output)

