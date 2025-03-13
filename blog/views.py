#from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy # importa reverse lazy
#Se importan las clases genericas para poder Crear, Actualizar o Borrar
from django.views.generic.edit import CreateView #UpdateView, DeleteView


class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'
    
# se agrego la nueva clase    
class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication-detail.html'   
# se agrego la forma para hacer la vista del create (modelo con template)
class PublicationCreateView(CreateView):
    model = Publication
    template_name = "publication-create.html"
    fields = ['title', 'body', 'author']
    def get_success_url(self):
        return reverse_lazy('publications-list')
    
#class PublicationlUpdateView(UpdateView):
 #   model = Publication
  #  template_name = ".html"

#class class PublicationDeleteView(DeleteView):
 #   model = Publication
  #  template_name = ".html"
    






# Create your views here.
