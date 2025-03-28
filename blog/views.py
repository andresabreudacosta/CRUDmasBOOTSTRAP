#from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy # importa reverse lazy para tener una direccion de retorno

#Se importan las clases genericas para poder Crear, Actualizar y Borrar
from django.views.generic.edit import (
                                        CreateView ,
                                       UpdateView , 
                                       DeleteView)

#se agregan servicios de autenticacion y permisos
#se importan los mixins para la autenticacion y permisos
from django.contrib.auth.mixins import (
                                        LoginRequiredMixin, 
                                        UserPassesTestMixin
                                        )



class PublicationListView(ListView):
    #se agrega el mixin para la autenticacion
    model = Publication
    template_name = 'publications-list.html'
    


# se agrego la nueva clase    
class PublicationDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    #se agrega el mixin para la autenticacion y el de permisos
    
    model = Publication
    template_name = 'publication-detail.html'
    
    def test_func(self):
        obj=self.get_object()
        #se verifica si el usuario es el autor del objeto       
        return self.request.user == obj.author
    
    
       
# se agrego la forma para hacer la vista del create (modelo con template)
# el orden de los parametros importa en el create view
class PublicationCreateView(LoginRequiredMixin, CreateView):
    #se agrega el mixin para la autenticacion y el de permisos      
    model = Publication
    template_name = "publication-create.html"
    fields = ['title', 'body', 'author']
    
    #def get_success_url(self):
    #    return reverse_lazy('publications-list')
    #se agrega la redireccion al crear el objeto
    
    
class PublicationUpdateView(UpdateView , LoginRequiredMixin, UserPassesTestMixin):
    #se agrega el mixin para la autenticacion y el de permisos
    
    model = Publication
    template_name = "publication-update.html"
    fields = ['title', 'body']

    def test_func(self):
        obj=self.get_object()
        #se verifica si el usuario es el autor del objeto
        return self.request.user == obj.author
    
class PublicationDeleteView(DeleteView , LoginRequiredMixin, UserPassesTestMixin):
    #se agrega el mixin para la autenticacion y el de permisos
    model = Publication
    template_name = "publication-delete.html"
    success_url = reverse_lazy('publications-list')

    
    def test_func(self):
        obj=self.get_object()
        #se verifica si el usuario es el autor del objeto
        return self.request.user == obj.author
    




# Create your views here.
