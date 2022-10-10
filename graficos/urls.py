from django.urls import path
from . import views
from .views import Graficos

urlpatterns = [
    path('graficos/', Graficos.as_view(), name="conecta"),

]




