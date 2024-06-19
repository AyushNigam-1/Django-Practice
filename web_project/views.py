from django.http import HttpResponse

def about(request):
    return HttpResponse("This is About page")

def course(request, courseid):
    return HttpResponse(courseid)