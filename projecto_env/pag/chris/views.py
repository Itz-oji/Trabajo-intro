from cgitb import reset
from html.entities import html5
from django.shortcuts import render, redirect
from .forms import NewRegister
from django.http import HttpResponse
from django.template import loader
from .services import get_fotogato, get_fotoperro
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  

# Create your views here.

def home(request):
    return render(request, 'home.html')
def galeria(request):
    return render(request, 'galeria.html')
def prueba(request):
    return render(request, 'registration/login.html')
# def login(request):
    return render(request, 'vistalogin.html')
def perropag(request):
    return render(request, 'perro.html')
def gatopag(request):
    return render(request, 'gato.html')
def mascota1pag(request):
    return render(request, 'mascotas.html')
def mascota2pag(request):
    return render(request, 'mascotass.html')
def login2(request):
    form = UserCreationForm()
    return render(request,'registration/login2.html',{'form': form})

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    return render(request, 'registration/register.html',{'form':NewRegister})

# def subirperro(request):
#     if request.method=="POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             return redirect('login')
#     else:
#         form=UserForm()
#     return render(request, 'app/lon.html',{
#         'form':form
#     })

def perro(request):
  template = loader.get_template('home.html')
  context = {
    'perrofoto': get_fotoperro(),
  }
  return HttpResponse(template.render(context, request))

def gatos(request):
  template = loader.get_template('home.html')
  context = {
    'gatofoto': get_fotogato(),
  }
  return HttpResponse(template.render(context, request))