# se van a definir las urls que se van a utilizar para la aplicación de cuentas.


from django.urls import path
# Se importa la vista SignUpView
from .views import SignUpView


urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
]
