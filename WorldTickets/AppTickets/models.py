from django.db import models

# Create your models here.
class Client(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.lastName}, {self.firstName}"
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['lastName']

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    date = models.DateField()
    soldOut = models.BooleanField()

    def __str__(self):
        return f"{self.event_name}, {self.date}"
        
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['date']
    
class Artist(models.Model):
    name = models.CharField(max_length=50)
    webpage = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"