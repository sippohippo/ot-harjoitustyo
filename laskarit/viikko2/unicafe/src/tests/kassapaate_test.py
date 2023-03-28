import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
    	self.kassapaate = Kassapaate()
    	self.maksukortti = Maksukortti(1000)

    # Alustus

    def test_oikea_aloitus_maara_rahaa(self):
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_alussa_nolla(self):
    	self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alussa_nolla(self):
    	self.assertEqual(self.kassapaate.maukkaat, 0)

    # Ostaminen kateisella

    def test_syo_edullisesti_kateisella_kasvattaa_kassaa(self):
    	self.kassapaate.syo_edullisesti_kateisella(240)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassaa(self):
    	self.kassapaate.syo_maukkaasti_kateisella(400)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_edullisen_ostaminen_kasvattaa_laskuria(self):
    	self.kassapaate.syo_edullisesti_kateisella(240)
    	self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_maukkaan_ostaminen_kasvattaa_laskuria(self):
    	self.kassapaate.syo_maukkaasti_kateisella(400)
    	self.assertEqual(self.kassapaate.maukkaat, 1)   

    def test_syo_edullisesti_kateisella_palauttaa_ylimenevan_osan(self):
    	self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_syo_maukkaasti_kateisella_palauttaa_ylimenevan_osan(self):
    	self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)

    def test_syo_edullisesti_kateisella_tasarahalla_palauttaa_nolla(self):
    	self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_syo_maukkaasti_kateisella_tasarahalla_palauttaa_nolla(self):
    	self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    	# Liian vahan rahaa

    def test_syo_edullisesti_kateisella_liian_vahan_palauttaa_rahan(self):
    	self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_syo_maukkaasti_kateisella_liian_vahan_palauttaa_rahan(self):
    	self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_syo_edullisesti_kateisella_liian_vahan_ei_kasvata_laskuria(self):
    	self.kassapaate.syo_edullisesti_kateisella(200)
    	self.assertEqual(self.kassapaate.edulliset, 0)    	

    def test_syo_maukkaasti_kateisella_liian_vahan_ei_kasvata_laskuria(self):
    	self.kassapaate.syo_maukkaasti_kateisella(200)
    	self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_liian_vahan_ei_kasvata_saldoa(self):	
    	self.kassapaate.syo_edullisesti_kateisella(200)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_liian_vahan_ei_kasvata_saldoa(self):    	
    	self.kassapaate.syo_maukkaasti_kateisella(200)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Kortilla ostaminen

    def test_syo_edullisesti_kortilla_palauttaa_true(self):
    	self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
    	self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortin_saldo_muuttuu(self):
    	self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    	self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_maukkaasti_kortin_saldo_muuttuu(self):
    	self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    	self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortilla_edullisen_ostaminen_kasvattaa_laskuria(self):
    	self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    	self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_maukkaan_ostaminen_kasvattaa_laskuria(self):
    	self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    	self.assertEqual(self.kassapaate.maukkaat, 1)

    	# Raha ei riita

    def test_kortilla_ei_riita_rahaa_syo_edullisesti_kortilla_palauttaa_false(self):
    	maksukortti = Maksukortti(100)
    	self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_kortilla_ei_riita_rahaa_syo_maukkaasti_kortilla_palauttaa_false(self):
    	maksukortti = Maksukortti(100)
    	self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_kortilla_ei_riita_rahaa_syo_edullisesti_kortin_saldo_ei_muutu(self):
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    	self.assertEqual(maksukortti.saldo, 100)

    def test_kortilla_ei_riita_rahaa_syo_maukkaasti_kortin_saldo_ei_muutu(self):
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    	self.assertEqual(maksukortti.saldo, 100)

    def test_kortilla_ei_riita_rahaa_kortilla_edullisen_ostaminen_ei_kasvata_laskuria(self):
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    	self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortilla_ei_riita_rahaa_kortilla_maukkaan_ostaminen_ei_kasvata_laskuria(self):
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    	self.assertEqual(self.kassapaate.maukkaat, 0)   


    	# Kortilla ostaessa kassan saldo ei muutu

    def test_syo_edullisesti_kortilla_ei_kasvata_saldoa(self):	
    	self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_kasvata_saldoa(self):    	
    	self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_liian_vahan_ei_kasvata_saldoa(self):	
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_liian_vahan_ei_kasvata_saldoa(self):    	
    	maksukortti = Maksukortti(100)
    	self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Rahan lataaminen

    def test_kortin_lataaminen_kasvattaa_kassaa(self):
    	self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortin_lataaminen_kasvattaa_kortin_saldoa(self):
    	self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
    	self.assertEqual(self.maksukortti.saldo, 2000)		    	

    def test_kortin_lataaminen_negatiivisella_palauttaa_none(self):
    	self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000), None)

    def test_kortin_lataaminen_negatiivisella_ei_muuta_kassaa(self):
    	self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 


