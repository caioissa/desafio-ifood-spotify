import sys
from flask import Blueprint, request

sys.path.append('./src')
from business_logic.song_recommender import SongRecommender

playlist_router = Blueprint('playlist_router', __name__)
sr = SongRecommender()

@playlist_router.route('/playlist')
def get():
    cityname = request.args.get('cityname')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    length = request.args.get('length')

    if cityname:
        if length:
            return sr.recommend_playlist_by_cityname(cityname, length), 200
        else:
            return sr.recommend_playlist_by_cityname(cityname), 200

    elif lat and lon:
        if length:
            return sr.recommend_playlist_by_latlon(lat, lon, length), 200
        else:
            return sr.recommend_playlist_by_latlon(lat, lon), 200

    else:
        return {
            'error': 'querystring should contain either cityname or lat and lon'
        }, 400
