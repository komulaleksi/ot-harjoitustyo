import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)

    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_maara_alussa_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_maara_alussa_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_vaihtoraha_oikein_syodessa_edullisesti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_kassa_oikein_syodessa_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_lounaiden_maara_kasvaa_syodessa_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_rahat_palautuvat_syodessa_edullisesti_kateisella_kun_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kassa_oikein_syodessa_edullisesti_kateisella_kun_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaiden_maara_ei_kasva_syodessa_edullisesti_kateisella_kun_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

        
    def test_vaihtoraha_oikein_syodessa_maukkaasti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_kassa_oikein_syodessa_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_lounaiden_maara_kasvaa_syodessa_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahat_palautuvat_syodessa_maukkaasti_kateisella_kun_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)

    def test_kassa_oikein_syodessa_maukkaasti_kateisella_kun_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaiden_maara_ei_kasva_syodessa_maukkaasti_kateisella_kun_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_kortilta_veloitetaan_oikein_syodessa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 9760)

    def test_korttimaksu_menee_lapi_syodessa_edullisesti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_lounaiden_maara_kasvaa_syodessa_edullisesti_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortin_rahamaara_ei_muutu_syodessa_edullisesti_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(100)

        self.assertEqual(kortti.saldo, 100)

    def test_korttimaksu_ei_mene_lapi_syodessa_edullisesti_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_lounaiden_maara_ei_kasva_syodessa_edullisesti_kortilla_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_rahamaara_ei_muutu_syodessa_edullisesti_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kortilta_veloitetaan_oikein_syodessa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 9600)

    def test_korttimaksu_menee_lapi_syodessa_maukkaasti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_lounaiden_maara_kasvaa_syodessa_maukkasti_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortin_rahamaara_ei_muutu_syodessa_maukkaasti_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 300)

    def test_korttimaksu_ei_mene_lapi_syodessa_maukkaasti_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_lounaiden_maara_ei_kasva_syodessa_maukkaasti_kortilla_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_syodessa_maukkaasti_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    
    def test_korttia_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 5000)

        self.assertEqual(self.kortti.saldo, 15000)

    def test_korttia_ladattaessa_kassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 5000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)

    def test_korttia_ladattaessa_negatiivisesti_kortin_saldo_ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -5000)

        self.assertEqual(self.kortti.saldo, 10000)

    def test_korttia_ladattaessa_negatiivisesti_kassa__ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -5000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)