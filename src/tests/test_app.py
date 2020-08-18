import sys

import unittest

sys.path.append('./src')
from app import app

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

if __name__ == '__main__':
    unittest.main()
