import requests
from flight_search import FlightSearch
from sheet import data
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
import smtplib

data_manager = DataManager()
# sheet_data = data
sheet_data = data_manager.get_destination()
fl = FlightSearch()
flight_data = FlightData()
for index in sheet_data:
    index["iataCode"] = fl.return_IATA(index["city"])
    res = flight_data.get_flights(index["iataCode"])
    if index["lowestPrice"] > res["price"]:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="", password="")
            connection.sendmail(from_addr="",
                                to_addrs="",
                                msg=f"Subject: New Flight Found \n\n Headline: Low price alert!Only{res["price"]}to "
                                    f"fly from {res["cityFrom"]}-{res["cityCodeFrom"]} to "
                                    f"{res["cityTo"]}-{res["cityCodeTo"]} from"
                                    f" {res["local_departure"].split("T"[0])} to {res["local_arrival"].split("T")[0]}")

pprint(sheet_data)
data_manager.sheet_data = sheet_data
data_manager.update()
