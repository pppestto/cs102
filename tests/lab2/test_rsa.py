import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt


class RsaTestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(n=2), True)

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        public_key, private_key = generate_keypair(17, 23)
        self.assertNotEqual(public_key, private_key)