import sys

import unittest

sys.path.append('./src')
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_run(self):
        response = self.app.get('/playlist?cityname=Campinas')
        self.assertEqual(response.status_code, 200)

    def test_playlist_length(self):
        response = self.app.get('/playlist?lat=20&lon=20')
        self.assertEqual(len(response.json['playlist']), 20)

    def test_unknown_cityname(self):
        response = self.app.get('/playlist?cityname=cdisaocjsaiocdjaio')
        self.assertEqual(response.status_code, 500)

    def test_invalid_lat(self):
        response = self.app.get('/playlist?lat=250&lon=20')
        self.assertEqual(response.status_code, 500)

    def test_invalid_lon(self):
        response = self.app.get('/playlist?lat=20&lon=250')
        self.assertEqual(response.status_code, 500)

    def test_playlist_length_query_100(self):
        response = self.app.get('/playlist?cityname=Campinas&length=100')
        self.assertEqual(len(response.json['playlist']), 100)

    def test_playlist_length_query_1(self):
        response = self.app.get('/playlist?cityname=Campinas&length=1')
        self.assertEqual(len(response.json['playlist']), 1)

if __name__ == '__main__':
    unittest.main()
