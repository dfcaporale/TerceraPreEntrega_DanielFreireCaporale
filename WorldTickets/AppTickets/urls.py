from django.urls import path
from AppTickets import views
#from .views import *

urlpatterns = [
    path('', views.home, name="home" ),
    path('events/', views.events, name="eventos" ),
    path('artists/', views.artists, name="artistas" ),
    path('clients/', views.clients, name="clientes" ),
    
    path('artist_form/', views.artistForm, name="add_artist_form" ),
    
    path('search_/', views.search_, name="search_" ),
    path('artist_search/', views.artistSearch, name="busca_artista" ),

    path('event_form/', views.eventForm, name="add_event_form" ),

    path('new_client/', views.clientForm, name="new_client_form" ),
]