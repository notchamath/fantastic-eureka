import os
import requests

SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_ENDPOINT = "https://api.sheety.co/8aa11738f65c35963040478cb15014cf/flightDealsTracker/prices/"
HEADER_S = {
    "Authorization": f"Bearer {SHEETY_KEY}",
}


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.wishlist = []
        self.read_spreadsheet()
        self.fill_missing_codes()

    def read_spreadsheet(self):
        res = requests.get(url=SHEETY_ENDPOINT, headers=HEADER_S)
        res.raise_for_status()
        self.wishlist = res.json()["prices"]

    def fill_missing_codes(self):
        for destination in self.wishlist:
            if destination["iataCode"] == "":
                print(destination["city"])

