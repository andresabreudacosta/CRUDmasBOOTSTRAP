#from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView

class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'
    
# se agrego la nueva clase    
class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication-detail.html'   

# Create your views here.
