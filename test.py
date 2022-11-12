from unittest import TestCase
from main import nod, nok


class TestMain(TestCase):
    def test_nod_1(self):
        self.assertEqual(12, nod(24, 36))

    def test_nod_2(self):
        self.assertEqual(12, nod(36, 24))

    def test_nod_3(self):
        self.assertEqual(1, nod(1, 24))

    def test_nod_4(self):
        self.assertEqual(1, nod(24, 1))

    def test_nok_1(self):
        self.assertEqual(72, nok(24, 36))

    def test_nok_2(self):
        self.assertEqual(72, nok(36, 24))

    def test_nok_3(self):
        self.assertEqual(24, nok(1, 24))

    def test_nok_4(self):
        self.assertEqual(24, nok(24, 1))
