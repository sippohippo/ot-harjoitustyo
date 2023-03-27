import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_vahenee_jos_rahaa_riittavasti(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_liian_vahan(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_rahaa_riittavasti(self):
        boolean_arvo = self.maksukortti.ota_rahaa(100)

        self.assertEqual(boolean_arvo, True)

    def test_metodi_palauttaa_false_jos_rahaa_ei_riittavasti(self):
        boolean_arvo = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(boolean_arvo, False)

