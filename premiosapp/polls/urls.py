#importa de djangourls la funcion path
from django.urls import path
#importa de si misma views
from . import views

urlpatterns = [
    path("", views.index, name="index")
]