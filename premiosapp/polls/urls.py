#importa de djangourls la funcion path
from django.urls import path
#importa de si misma views
from . import views

urlpatterns = [
    #example: /polls/
    path("", views.index, name="index"),
    #example: /polls/5
    path("<int:question_id>/", views.detail, name="detail"),
    #example: /polls/5/results
    path("<int:question_id>/results/", views.results, name="results"),
    #example: polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]