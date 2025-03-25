# Django imports
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
#
from django.urls import reverse_lazy
# Se importa la vista CreateView
from django.views.generic.edit import CreateView

# Se define la vista SignUpView que hereda de CreateView
class SignUpView(CreateView):
    # Se define la clase SignUpView que hereda de CreateView
    template_name = 'registration/signup.html'
    # Se define el template que se va a utilizar
    form_class = UserCreationForm
    # Se define el formulario que se va a utilizar
    success_url = reverse_lazy('login')
    # Se define la url de retorno

