# Ohjelmistotekniikka, harjoitustyö
Versio [Yatzy pelistä](https://fi.wikipedia.org/wiki/Yatzy), jossa tarkoitus on saada *viittä* noppaa heittämällä erilaisia lukujen yhdistelmiä.  

## Käynnistysohjeet
1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä ohjelma komennolla:
  
```bash
poetry run invoke start
```

- Ohjelmaa voi testata komennolla:

```bash
poetry run invoke test
```

- Testikattavuusraportin saa luotua komennolla:

```bash
poetry run invoke coverage-report
```

- Pylintin laatutarkastuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```

- Koodin voi automaattisesti formatoida komennolla:

```bash
poetry run invoke format
```

## Peliohjeet
1. Käynnistä peli yllä olevien ohjeiden mukaisesti.
2. Näet aloitusheiton antamat viisi noppaa.
- Voit lukita haluamasi nopat ruksamalla nopan järjestyslukua vastaavan laatikon.
3. Heitä noppia painamalla Heitä-painiketta.
- Lukittuja noppia ei heitetä uudelleen.
- Voit heittää noppia enintään kolme kertaa kierroksen aikana.
4. Valitse valikosta haluamasi pisteytyskategoria ja paina Valitse-näppäintä.
- Sinun ei tarvitse heittää noppia kaikkia kolmea kertaa, vaan voit valita kategorian jo aikaisemmilla heitoilla.
5. 15 kierroksen jälkeen (kun kaikki pisteytyskategoriat on käytetty) peli päättyy.
- Voit myös päättää pelin kesken kaiken painamalla Lopeta-näppäintä.
6. Pelin päätyttyä näet lopullisen pistetuloksesi ja listan kymmenestä parhaasta pistetuloksesta (Ensimmäisellä pelikerralla tämä on tietysti tyhjä).
7. Kirjoita Nimimerkki-laatikkoon haluamasi nimimerkki ja paina Tallenna-näppäintä, jolloin tuloksesi tallennetaan.
8. Lopeta peli painamalla Poistu-näppäintä.

## Pisteytyskategoriat
- Ykköset-Kuutoset: Kyseistä silmälukua vastaavien noppien arvo lasketaan yhteen.
- Yksi pari: Kaksi samaa silmälukua lasketaan yhteen.
- Kaksi paria: Kaksi paria samaa silmälukua lasketaan yhteen.
- Kolmoisluku: Kolme samaa silmälukua lasketaan yhteen.
- Nelosluku: Neljä samaa silmälukua lasetaan yhteen.
- Pieni suora: Silmäluvut [1, 2, 3, 4, 5], 15 pistettä.
- Suuri suora: Silmäluvut [2, 3, 4, 5, 6], 20 pistettä.
- Täyskäsi: Kolmoisluku ja pari, pisteet lasketaan yhteen.
- Sattuma: Mitkä tahansa silmäluvut, lasketaan yhteen.
- Yatzy: Viisi samaa silmälukua, 50 pistettä.

## Releaset
[Viikko 5](https://github.com/komulaleksi/ot-harjoitustyo/releases/tag/viikko5)  
[Viikko 6](https://github.com/komulaleksi/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio
[Vaativuusmäärittely](https://github.com/komulaleksi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[Työaikakirjanpito](https://github.com/komulaleksi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)  
[Changelog](https://github.com/komulaleksi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)  
[Arkkitehtuuri](https://github.com/komulaleksi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Testaus](https://github.com/komulaleksi/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
