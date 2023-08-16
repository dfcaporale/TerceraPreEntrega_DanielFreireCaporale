## WorldTickets Project

### Package download and setup:

`$ git clone https://github.com/dfcaporale/TerceraPreEntrega_DanielFreireCaporale.git`

`$ cd TerceraPreEntrega_DanielFreireCaporale/WorldTickets/`

`$ python manage.py runserver`

Open a web browser and navigate to the homepage using localhost:8000.

The website is dedicated to a ticket-selling service.

Currently, the app allows navigation through the buttons: Home, Artists, Events, and Search Artist.

The database includes the modules: Artist, Event, and Client; the latter can be accessed through [localhost:8000/clients/](http://localhost:8000/clients/)

New data can be added using the following forms:
- Add a new artist: [localhost:8000/artist_form/](http://localhost:8000/artist_form/)
- Add a new event: [localhost:8000/event_form/](http://localhost:8000/event_form/)
- Add a new client: [localhost:8000/new_client/](http://localhost:8000/new_client/)
