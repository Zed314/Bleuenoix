from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def home(request):
    #return HttpResponse("""<h1>WESH</h1>""")
    return redirect(view_redirection, "Redirigé!")

def number(request,numb,numb2):
    return HttpResponse(numb2)

def view_redirection(request, message="ntm"):
    return HttpResponse(message)

def date(request):
    return render(request,'blog/date.html', {'date':datetime.now(), 'req':request})

def lp(request):
    return HttpResponse("i")

def accueil(request):
    return render(request, 'blog/accueil.html')

    