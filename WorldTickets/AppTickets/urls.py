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
    path('artist_search/', views.artistSearch, name="artist_search" ),
]