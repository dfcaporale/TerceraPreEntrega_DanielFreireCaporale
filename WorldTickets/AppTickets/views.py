from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppTickets.forms import ArtistForm, EventForm, ClientForm


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
    contexto = {'clientes': Client.objects.all()}
    return render(request, "AppTickets/clients.html", contexto)



def artistForm(request): 
    if request.method == "POST":
        miForm = ArtistForm(request.POST) # info comes from the html
        if miForm.is_valid():
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



def eventForm(request): 
    if request.method == "POST":
        miForm = EventForm(request.POST) # info comes from the html
        if miForm.is_valid():
            event_name_in = miForm.cleaned_data.get('event_name')
            artist_in = miForm.cleaned_data.get('artist')
            country_in = miForm.cleaned_data.get('country')
            city_in = miForm.cleaned_data.get('city')
            venue_in = miForm.cleaned_data.get('venue')
            date_in = miForm.cleaned_data.get('date')
            soldOut_in = False #miForm.cleaned_data.get('sold_out')
            event_in = Event(event_name=event_name_in, artist=artist_in,
                             country=country_in, city=city_in, venue=venue_in,
                             date=date_in, soldOut=soldOut_in)
            event_in.save()
            return render(request, "AppTickets/base.html")
    else: # if first time called
        miForm = EventForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/eventForm.html", contexto)

def clientForm(request): 
    if request.method == "POST":
        miForm = ClientForm(request.POST) # info comes from the html
        if miForm.is_valid():
            client_name_in = miForm.cleaned_data.get('name')
            client_surname_in = miForm.cleaned_data.get('surname')
            client_email_in = miForm.cleaned_data.get('email')
            client_in = Client(firstName=client_name_in, lastName=client_surname_in,
                             email=client_email_in)
            client_in.save()
            return render(request, "AppTickets/clients.html")
    else: # if first time called
        miForm = ClientForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/clientForm.html", contexto)