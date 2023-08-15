from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppTickets.forms import ArtistForm


# Create your views here.
def home(request):
    return render(request, "AppTickets/home.html")

def events(request):
    contexto = {'eventos': Event.objects.all()}
    return render(request, "AppTickets/events.html", contexto)

def artists(request):
    contexto = {'artistas': Artist.objects.all()}
    return render(request, "AppTickets/artists.html", contexto)

def clients(request):
    return render(request, "AppTickets/clients.html")



def artistForm(request): 
    if request.method == "POST":
        miForm = ArtistForm(request.POST) # info comes from the html
        if miForm.is_valid:

            artist_name = miForm.cleaned_data.get('name')
            artist_webpage = miForm.cleaned_data.get('webpage')
            artist = Artist(name=artist_name, webpage=artist_webpage)
            artist.save()
            return render(request, "AppTickets/base.html")
    else: # if first time called
        miForm = ArtistForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/artistForm.html", contexto)

def search_(request):
    if request.GET['search']:
        pattern = request.GET['search']
        artistas_ = Artist.objects.filter(name__icontains=pattern)
        contexto = {"artistas": artistas_, 'title': f'Artists containing the pattern "{pattern}"'}
        return render(request, "AppTickets/artists.html", contexto)
    return HttpResponse("Please, indicate a pattern to be searched")

def artistSearch(request):
    return render(request, "AppTickets/artistSearch.html")
