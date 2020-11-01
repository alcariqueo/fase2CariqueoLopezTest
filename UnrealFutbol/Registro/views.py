from django.shortcuts import render
from . models import Usuario, Partido
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse

def index(request):

    return render(
        request,
        'index.html',
    )

def login(request):

    return render(
        request,
        'login.html',
    ) 

def registro(request):

    return render(
        request,
        'registro.html',
    )  

def terminos(request):

    return render(
        request,
        'terminos.html',
    ) 
def galeria(request):

    return render(
        request,
        'galeria.html',
    )

def apuesta(request):

    return render(
        request,
        'apuesta.html',
    )             

class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['email', 'fechaN', 'telefono', 'password']

class UsuarioDelete(DeleteView):
    model = Usuario
    def get_success_url(self):
        return reverse('index')
class UsuarioDetailView(generic.DetailView):
    model=Usuario

class PartidoListView(generic.ListView):
    model = Partido
class PartidoDetailView(generic.DetailView):
    model = Partido
