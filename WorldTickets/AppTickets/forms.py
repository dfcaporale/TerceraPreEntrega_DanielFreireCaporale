from django import forms

class ArtistForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    webpage = forms.CharField(max_length=50, required=True)