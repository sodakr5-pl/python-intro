import unittest
from app import email_check, oblicz, sortowanie, konwertuj_date, palindrom

class TestFunkcje(unittest.TestCase):

    def test_email_poprawny(self):
        self.assertTrue(email_check("oskar@o2.pl"))

    def test_email_brak_małpy(self):
        self.assertFalse(email_check("oskaro2.pl"))

    def test_email_pusty(self):
        self.assertFalse(email_check(""))

    
    def test_pole_trójkąta(self):
        self.assertEqual(oblicz(2,3), 3)

   
    def test_sortowanie(self):
        self.assertEqual(sortowanie([3,1,2]), [1,2,3])

    
    def test_konwersja(self):
        self.assertEqual(konwertuj_date("09-11-2025"), "2025/11/09")

   
    def test_palindrom(self):
        self.assertTrue(palindrom("kajak"))

if __name__ == "__main__":
    unittest.main()
