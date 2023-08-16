## WorldTickets Project

### Package download and setup:

`$ git clone https://github.com/dfcaporale/TerceraPreEntrega_DanielFreireCaporale.git`

`$ cd TerceraPreEntrega_DanielFreireCaporale/WorldTickets/`

`$ python manage.py runserver`

Open web browser and navigate to the homepage through [localhost:8000](http://localhost:8000)

The site is devoted to a tickets-sell service.

So far, the app allows navigation through the buttons: `Home`, `Artists`, `Events` and `Search Artist`.

The database contains the modules: `Artist`, `Event` and `Client`; the last is seen through [localhost:8000/clients/](http://localhost:8000/clients/).

New data can be added with the following forms:
- New artist: [localhost:8000/artist_form/](http://localhost:8000/artist_form/)
- New event: [localhost:8000/event_form/](http://localhost:8000/event_form/)
- New client: [localhost:8000/new_client/](http://localhost:8000/new_client/)


