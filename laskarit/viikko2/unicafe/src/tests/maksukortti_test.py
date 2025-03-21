import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_saldo_pienenee_ottaessa_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_vahene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_ottaminen_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahan_ottaminen_palauttaa_false_jos_ottaa_liikaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroissa_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")