classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu "1" -- "1" Aloitus
    Ruutu "1" -- "1" Vankila
    Ruutu "1" -- "1" Sattuma_ja_yhteismaa
    Ruutu "1" -- "1" Asemat_ja_laitokset
    Ruutu  --  Kadut
    Kadut -- Nimi
    Monopolipeli -- Vankila
    Monopolipeli -- Aloitus
    Sattuma_ja_yhteismaa -- Kortit
    Kortit -- Toiminto
    Katu "4" -- "4" Talo
    Katu "1" -- "1" Hotelli
    Pelaaja -- Katu
    Pelaaja -- Raha