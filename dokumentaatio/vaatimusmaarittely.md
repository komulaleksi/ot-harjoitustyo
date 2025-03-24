# Vaativuusmäärittely

## Sovelluksen tarkoitus
Tarkoitus on tehdä versio [**Yatzy**](https://en.wikipedia.org/wiki/Yahtzee) pelistä, jossa tarkoitus on saada viittä noppaa heittämällä erilaisia lukujen yhdistelmiä. Eri yhdistelmät on pisteytetty eri tavoin ja pelin idea onkin saavutta mahdollisimman korkea lopullinen pistetulos. Peli tulee olemaan yksinpeliversio, joskin eri pelaajat voivat kilpailla toisiaan vastaan pisteiden perusteella.

## Suunnitellut toiminnallisuudet
- Peli koostuu 13 kierroksesta
    - Joka kierroksella käyttäjä heittää viittä noppaa kolme eri kertaa
    - Käyttäjä voi lukita haluamallaan tavalla 0-5 noppaa, jolloin niitä ei arvota uudestaan seuraavilla heitoilla
    - Kolmen heiton jälkeen käyttäjä voi tallentaa saadun pistetuloksen yhteen kategoriaan riippuen heittojen lopputuloksesta
- Käyttäjä voi tallentaa pelin lopuksi saadun pistetuloksen taulukkoon omalla nimimerkillään
    - Taulukoon on tallennettu 10 parasta pistetulosta
    - Käyttäjällä voi olla monta tulosta samalla nimimerkillä

## Jatkokehitysideoita
- Hienompi graafinen liittymä
- Kenties mahdollisuus pelata kaksinpeliä
    - Tällöin vuoro siirtyisi jokaisen kierrosen jälkeen toiselle käyttäjälle, joka mahdollistaisi samanaikaisen kilpailun.
- Pelin sisäinen ohjekirja/pisteytystaulukko