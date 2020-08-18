import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyInterface():
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id='20fd0b23aa5a44a3a369e483e9d216e5',
            client_secret='cf98548e2ab343d8b2afe04808637f04'
            )
        )

    def get_playlist_by_genre(self, genre, length=20):
        lista = self.sp.recommendations(seed_genres=[genre], limit=length)['tracks']
        return [e['name'] for e in lista]
