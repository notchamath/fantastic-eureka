import os
import requests

FLIGHT_KEY = os.environ["FLIGHT_KEY"]
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com"
HEADER = {
    "apikey": FLIGHT_KEY,
}


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.flights = []

    # Get IATA Code for given city from API
    def get_city_code(self, city):
        location_endpoint = f"{FLIGHT_ENDPOINT}/locations/query/"
        params = {
            "term": city
        }

        res = requests.get(
            url=location_endpoint,
            headers=HEADER,
            params=params,
        )
        res.raise_for_status()
        return res.json()["locations"][0]["code"]

    def search_flights(self, params):
        search_endpoint = f"{FLIGHT_ENDPOINT}/v2/search"

        res = requests.get(
            url=search_endpoint,
            headers=HEADER,
            params=params,
        )
        res.raise_for_status()

        data = res.json()
        if data["_results"] > 0:
            self.flights.append(data["data"])
