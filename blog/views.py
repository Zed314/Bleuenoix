from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    #return HttpResponse("""<h1>WESH</h1>""")
    return redirect(view_redirection, "Redirigé!")

def number(request,numb,numb2):
    return HttpResponse(numb2)

def view_redirection(request, message="ntm"):
    return HttpResponse(message)