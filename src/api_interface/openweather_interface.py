import requests

class OpenweatherInterface:
    def __init__(self):
        self.appid = 'b77e07f479efe92156376a8b07640ced'
        self.query = ''

    def fetch_by_cityname(self, cityname):
        self.query = 'q={}'.format(cityname)
        return self.fetch()

    def fetch_by_latlon(self, lat, lon):
        self.query = 'lat={}&lon={}'.format(lat, lon)
        return self.fetch()

    def fetch(self):
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?{}&appid={}&units=metric'
                         .format(self.query, self.appid))
        if (r.status_code == 200):
            return r.json()

    def get_temp_by_cityname(self, cityname):
        return self.fetch_by_cityname(cityname)['main']['temp']

    def get_temp_by_latlon(self, lat, lon):
        return self.fetch_by_latlon(lat, lon)['main']['temp']
