import os
import requests

SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_ENDPOINT = "https://api.sheety.co/8aa11738f65c35963040478cb15014cf/flightDealsTracker/prices"
HEADER = {
    "Authorization": f"Bearer {SHEETY_KEY}",
}


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.wishlist = []
        self.read_spreadsheet()

    def read_spreadsheet(self):
        res = requests.get(url=SHEETY_ENDPOINT, headers=HEADER)
        res.raise_for_status()
        self.wishlist = res.json()["prices"]

    # Update "IATA Code" section on Google Sheet
    def fill_missing_codes(self, idx, city_code):
        edit_url = f"{SHEETY_ENDPOINT}/{idx + 2}"
        params = {
            "price": {
                "iataCode": city_code
            }
        }
        res = requests.put(url=edit_url, headers=HEADER, json=params)
        res.raise_for_status()
