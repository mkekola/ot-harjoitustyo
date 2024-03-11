import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    #kortin saldo alussa oikein
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    #rahan lataaminen kasvattaa saldoa oikein
    def test_kortille_latautuu_saldo_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    #rahan ottaminen toimii oikein
    def test_kortilta_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 900)

    #saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_otto_ei_onnistu(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    #metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_ottaminen_palauttaa_true_jos_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)

    def test_str_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldo_euroina_toimii_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)


