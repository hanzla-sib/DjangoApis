from django.http import HttpResponse

def Homepage(request):
    print("Home page requeste")
    return HttpResponse('this is home page')