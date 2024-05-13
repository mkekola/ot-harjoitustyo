# Käyttöohje

## Ohjelman käynnistys

Riippuvuuksien asennus

```
poetry install
```

Ohjelman suorittaminen

```
poetry run invoke start
```

## Aloitusnäkymä

Aloitusnäkymässä käyttäjällä vaihtoehtoina on:

- Rekisteröidä uusi käyttäjä kirjoittamalla komentoriville '1'
- Kirjautua sisään kirjoittamalla komentoriville '2'
- Sulkea sovellus kirjoittamalla komentoriville '3'

## Rekisteröityminen

- Rekisteröityminen tapahtuu luomalla itselleen ensin käyttäjätunnus ja sen jälkeen salasana.
- Jos käyttäjätunnus on jo käytössä ohjelma antaa virheilmoituksen 'Username already exists'.
- Onnistuneen rekisteröitymisen jälkeen käyttäjän on mahdollista siirtyä kirjautumisnäkymään kirjoittamalla komentoriville '2' tai poistua sovelluksesta kirjoittamalla '3'.

## Kirjautuminen

- Kirjautuminen tapahtuu syöttämällä ensin luotu käyttäjätunnus ja sen jälkeen salasana.
- Jos käyttäjätunnusta ei löydy tai salasana ei ole oikea niin sovellusantaa virheilmoituksen 'Login failed.'
- Onnistuneen kirjautumisen jälkeen käyttäjä pääsee sovellusnäkymään, jossa käyttäjä voi listata omat tallentamansa hahmot kirjoittamalla komentoriville '1' tai luoda uuden hahmon kirjoittamalla '2'.
- Sovelluksesta pääsee kirjautumaan ulos kirjoittamalla komentoriville '3'.

## Uuden hahmon luominen

- Uuden hahmon generoinnin jälkeen käyttäjällä on mahdollisuus tallentaa luotu hahmo kirjoittamalla komentoriville vastauksen 'yes'.
- Vaihtoehtoisesti jos käyttäjä ei halua tallentaa hahmoa tulee kirjoittaa 'no'.
- Tämän jälkeen käyttäjän on mahdollista joko tarkastella tallennettuja hahmoja, luoda uusi hahmo tai kirjautua ulos.
