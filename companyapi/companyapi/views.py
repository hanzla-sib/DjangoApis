from django.http import HttpResponse

def Homepage(request):
    print("Home page requested")
    return HttpResponse('this is home page')