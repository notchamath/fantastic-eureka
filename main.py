# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

# Get missing IATA Code from Flight API and update Google sheets
wishlist = data_manager.wishlist
for idx in range(len(wishlist)):
    if wishlist[idx]["iataCode"] == "":
        city = wishlist[idx]["city"]
        # Get city code
        city_code = flight_search.get_city_code(city)
        # Update google sheet
        data_manager.fill_missing_code(idx, city_code)

# Read Google sheets again once missing info is updated
data_manager.read_spreadsheet()

# Search for Flights
wishlist = data_manager.wishlist
flight_params = flight_data.get_flight_data()

for destination in wishlist:
    flight_params["price_to"] = destination["lowestPrice"]
    flight_params["fly_to"] = destination["iataCode"]

    flight_search.search_flights(flight_params)

# Send notification
available_flights = flight_search.flights
if len(available_flights) > 0:
    for trip in available_flights:
        for flight in trip:
            notification_manager.send_text(flight)
