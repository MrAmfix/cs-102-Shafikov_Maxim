import unittest
from src.lab2.vigenre import encrypt_vigenere
from src.lab2.vigenre import decrypt_vigenere

class TestCaesar(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("CHICKEN", "KFC"), "MMKMPGX")
        self.assertEqual(encrypt_vigenere("genshin impact", "anime"), "grvelia qytapb")
        self.assertEqual(encrypt_vigenere("88005553535 :)", "MONEY"), "88005553535 :)")
        self.assertEqual(encrypt_vigenere("RANDOM.RANDINT(0,100)", "RANDOM"), "IAAGCY.IAAGWZK(0,100)")
        self.assertEqual(encrypt_vigenere("UNITED STATES", "USA"), "OFINWD MLANWS")
    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("UNITED KINGDOM", "UK"), "ADOJKT QYTWJES")
        self.assertEqual(decrypt_vigenere("rickroll ** hehe", "meme"), "feqgfkzh ** vava")
        self.assertEqual(decrypt_vigenere("kronbars team 666", "sport"), "scawiice clix 666")
        self.assertEqual(decrypt_vigenere("pavel durov 555 telegram", "vk"), "uqauq tzhtl 555 yuqulhfc")

if __name__ == "__main__":
    unittest.main()