import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyInterface():
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=os.environ['SPOTIFY_CLIENT_ID'],
            client_secret=os.environ['SPOTIFY_SECRET']
            )
        )

    def get_playlist_by_genre(self, genre, length=20):
        lista = self.sp.recommendations(seed_genres=[genre], limit=length)['tracks']
        return [e['name'] for e in lista]
