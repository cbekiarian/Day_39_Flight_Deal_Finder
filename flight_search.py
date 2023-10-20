import requests

URL = "https://api.tequila.kiwi.com/locations/query"
KEY =
class FlightSearch:
    def __init__(self):
        self.headers = {
            'accept': 'application/json',
            'apikey': KEY
        }


    def return_IATA(self,name):
        params = {
            'term': name,
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 10,
            'active_only': True,
            'sort': 'name'
        }
        response = requests.get(url=URL,params= params,headers=self.headers)
        response.raise_for_status()
        res = response.json()["locations"][0]["code"]
        return res
