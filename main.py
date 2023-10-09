# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

# Get missing IATA Code from Flight API and update Google sheets
wishlist = data_manager.wishlist
for idx in range(len(wishlist)):
    if wishlist[idx]["iataCode"] == "":
        city = wishlist[idx]["city"]
        # Get city code
        city_code = flight_search.get_city_code(city)
        # Update google sheet
        data_manager.fill_missing_code(idx, city_code)


