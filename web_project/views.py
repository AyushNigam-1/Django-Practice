from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # data={
    #     "title":"wow",
    #     "clist":[
    #         {"name":"Ayush" , "age":"16"},
    #         {"name":"Ayush","age":"18"},
    #         {"name":"Ayush","age":"19"}
    #         ]
    # }
    print(request.GET['ipt'])
    print(request.GET.get('ipt'))
    # try:
    #     ipt1 = request.GET['ipt']
    #     ipt2 = request.GET['ipt2']
    #     print("result" ,ipt1+ipt2)
    # except:
    #     pass
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def course(request, courseid):
    return HttpResponse(courseid)