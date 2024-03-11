import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_kassan_rahamaara_oikein(self): 
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edulliset_lounaat_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_maukkaat_lounaat_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_toimii_edullisesti(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kateisosto_toimii_maukkaasti(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kateisosto_ei_riittava_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_ei_riittava_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_toimii_edullisesti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_korttiosto_toimii_maukkaasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo_euroina(), 6)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttiosto_ei_riittava_edullinen(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo_euroina(), 1)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttiosto_ei_riittava_maukas(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo_euroina(), 1)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)

    def test_kortille_lataaminen_toimii(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 20)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1010)

    
    def test_kortille_lataaminen_negatiivinen_summa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -10000)
        self.assertEqual(self.kortti.saldo_euroina(), 10)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)