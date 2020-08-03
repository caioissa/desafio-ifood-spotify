import sys

sys.path.append('./src')
from api_interface.openweather_interface import OpenweatherInterface
from api_interface.spotify_interface import SpotifyInterface

class SongRecommender():
    def __init__(self):
        self.oi = OpenweatherInterface()
        self.si = SpotifyInterface()

    def recommend_playlist_by_cityname(self, cityname, length=20):
        temp = self.oi.get_temp_by_cityname(cityname)
        return self.get_playlist_by_temperature(temp, length)

    def recommend_playlist_by_latlon(self, lat, lon, length=20):
        temp = self.oi.get_temp_by_latlon(lat, lon)
        return self.get_playlist_by_temperature(temp, length)

    def get_playlist_by_temperature(self, temp, length=20):
        genre = self.get_genre_by_temperature(temp)
        return {'genre': genre, 'playlist': self.si.get_playlist_by_genre(genre, length)}

    def get_genre_by_temperature(self, temp):
        if temp > 30:
            return 'party'
        elif temp >= 15:
            return 'pop'
        elif temp >= 10:
            return 'rock'
        else:
            return 'classical'
