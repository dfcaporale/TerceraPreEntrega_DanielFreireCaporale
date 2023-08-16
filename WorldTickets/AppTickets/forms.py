from django import forms

class ArtistForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    webpage = forms.CharField(max_length=50, required=True)

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=50, required=True)
    artist = forms.CharField(max_length=50, required=True)
    country = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    venue = forms.CharField(max_length=50, required=True)
    date = forms.DateField(required=True)
    # sold_out = forms.BooleanField()

class ClientForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)