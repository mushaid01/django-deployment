from django.shortcuts import render

# Create your views here.

def index(request):
    dict={'text':'hello','num':100}
    return render(request,"basic_app/index.html",dict)


def other(request):
    return render(request,"basic_app/other.html")

def relative(request):
    return render(request,"basic_app/relative.html")
