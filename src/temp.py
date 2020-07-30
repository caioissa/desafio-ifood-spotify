import sys
from business_logic.song_recommender import SongRecommender
args = sys.argv
args.pop(0)

sr = SongRecommender()

if len(args) == 1:
    print('recommendation for city: {}'.format(args[0]))
    print(sr.recommend_playlist_by_cityname(args[0]))
elif len(args) == 2:
    print('recommendation for latlon: {} {}'.format(args[0], args[1]))
    print(sr.recommend_playlist_by_latlon(args[0], args[1]))
else:
    print('please insert one arg for cityname or two for lat lon')
