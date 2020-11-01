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
