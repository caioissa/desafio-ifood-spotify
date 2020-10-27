# Desafio Ifood Spotify
### Flask REST API from [ifood challenge for spotify playlist recommendation](https://github.com/ifood/vemproifood-backend)
This solution contains an endpoint for spotify playlist recommendations based on location and weather stats. It accesses Spotify API via the spotipy library and Openweather API.
## Installation
Create a virtualenv and run:
```bash
pip install -r requirements.txt
```
## Documentation
The api contains a single endpoint '/playlist' which requires either one of these set of query params:
1. `cityname` - cityname for recommendation
2. `lat` & `lon` - lat and lon for recommendation
Besides, it also accepts a optional param:
* `length` - length of recommended list, default = 20 
## Usage
1. To setup Spotify Keys, set environment variables:
```bash
export SPOTIFY_CLIENT_ID={your_id}
export SPOTIFY_SECRET={your_secret}
```
2. To run the app:
```bash
python src/app.py
```
3. Test in your browser!
```
http://127.0.0.1:5000/playlist?cityname={your city name}
```
```
http://127.0.0.1:5000/playlist?lat={your latitude}&lon={your longitude}&length=35
```
