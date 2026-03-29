# Keskustelupalsta
(Inspiraationa esim. Reddit ja Suomi24 tyyliset palvelut)

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Lisäksi käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan lisäämiään aiheita.
- Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät aiheet.
- Käyttäjä pystyy etsimään aiheita hakusanalla tai muulla perusteella. 
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät aiheet ja kommentit.
- Käyttäjä pystyy valitsemaan aiheelle yhden tai useamman kategorian. Mahdolliset kategoriat ovat esim. Sarjat ja elokuvat, Pelit, Anime ja Manga, Ruoka, Eläimet, Suhteet jne.
- Sovelluksessa on pääasiallisen aiheen noston lisäksi aiheeseen kommentointi, joka jatkaa keskustelua. 

# asennus
Asenna flask-kirjasto:

Linux: $ pip install flask
Windows: pip install Flask

Luo tietokannan taulut ja lisää alkutiedot:

Linux: $ sqlite3 database.db < schema.sql
Windows: sqlite3.exe database.db ".read schema.sql"

Käynnistys:

Linux: $ flask run 
Windows: flask run
