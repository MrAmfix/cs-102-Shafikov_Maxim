import unittest
from src.lab2.caesar import encrypt_caesar
from src.lab2.caesar import decrypt_caesar

class TestCaesar(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('Pythonist'), 'Sbwkrqlvw')
        self.assertEqual(encrypt_caesar('ITMO University'), 'LWPR Xqlyhuvlwb')
        self.assertEqual(encrypt_caesar('Shaurma ili Shaverma?'), 'Vkdxupd lol Vkdyhupd?')
        self.assertEqual(encrypt_caesar('4ERT.ILA'), '4HUW.LOD')
        self.assertEqual(encrypt_caesar('423---43..'), '423---43..')
        self.assertEqual(encrypt_caesar('XYZ.xyz'), 'ABC.abc')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('Xqlwhg Vwdwhv'), 'United States')
        self.assertEqual(decrypt_caesar('ABC.abc'), 'XYZ.xyz')
        self.assertEqual(decrypt_caesar('F++, Sbwkrq, Mdyd'), 'C++, Python, Java')
        self.assertEqual(decrypt_caesar('+-.778--'), '+-.778--')
        self.assertEqual(decrypt_caesar('DEF>ABC'), 'ABC>XYZ')
        self.assertEqual(decrypt_caesar('jhqvklq lpsdfw'), 'genshin impact')

if __name__ == "__main__":
    unittest.main()