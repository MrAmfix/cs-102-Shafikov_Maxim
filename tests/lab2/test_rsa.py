import unittest
from src.lab2.rsa import encrypt
from src.lab2.rsa import decrypt
from src.lab2.rsa import generate_keypair

class TestRsa(unittest.TestCase):

    def testRSA(self):
        pub, priv = generate_keypair(13, 37)
        self.assertEqual(decrypt(pub, encrypt(priv, "Vlad Tereshenko")), "Vlad Tereshenko")
        self.assertEqual(decrypt(pub, encrypt(priv, "KVAS80rub-KEFIR60rub")), "KVAS80rub-KEFIR60rub")
        self.assertEqual(decrypt(pub, encrypt(priv, "Hearts of iron 4")), "Hearts of iron 4")