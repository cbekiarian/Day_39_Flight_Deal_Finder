import requests
from pprint import pprint
SHEETY_ENDPOINT ="https://api.sheety.co/e11f87f0122ceda5ca43b5a02b935667/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data= {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return self.sheet_data
    def update(self):
        for row in self.sheet_data:

            datas = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url =f"{SHEETY_ENDPOINT}/{row["id"]}" ,
                json= datas)
            response.raise_for_status()


