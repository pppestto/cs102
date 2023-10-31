import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenereTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere(plaintext="PYTHON", keyword="A"), 'PYTHON')
        self.assertEqual(encrypt_vigenere(plaintext="ATTACKATDAWN", keyword="LEMON"), 'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere(plaintext="python", keyword="a"), "python")

    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere(ciphertext="PYTHON", keyword="A"), 'PYTHON')
        self.assertEqual(decrypt_vigenere(ciphertext="python", keyword="a"), "python")
        self.assertEqual(decrypt_vigenere(ciphertext="LXFOPVEFRNHR", keyword="LEMON"), 'ATTACKATDAWN')
