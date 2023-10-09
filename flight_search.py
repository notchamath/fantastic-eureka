import os
import requests
import datetime

FLIGHT_KEY = os.environ["FLIGHT_KEY"]
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com"
HEADER = {
    "apikey": FLIGHT_KEY,
}
FLY_FROM_CITY = "NYC"


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.flights = []

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

    def search_flights(self):
        today = datetime.datetime.now()
        search_begin_date = (today + datetime.timedelta(7)).strftime("%d/%m/%Y")
        search_end_date = (today + datetime.timedelta(187)).strftime("%d/%m/%Y")
        nights_in_dst_from = 7
        nights_in_dst_to = 28

        search_endpoint = f"{FLIGHT_ENDPOINT}/v2/search"
        params = {
            "fly_from": FLY_FROM_CITY,
            "fly_to": "LON",
            "date_from": search_begin_date,
            "date_to": search_end_date,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "curr": "USD",

        }

        res = requests.get(
            url=search_endpoint,
            headers=HEADER,
            params=params,
        )
        res.raise_for_status()

        print(res.json())
