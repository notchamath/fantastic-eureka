import os
import requests

FLIGHT_KEY = os.environ["FLIGHT_KEY"]
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/locations/query/"
HEADER = {
    "apikey": FLIGHT_KEY,
}


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.flights = []

    def get_city_code(self, city):
        params = {
            "term": city
        }

        res = requests.get(url=FLIGHT_ENDPOINT, headers=HEADER, params=params)
        res.raise_for_status()
        return res.json()["locations"][0]["code"]
