import datetime

FLY_FROM_CITY = "NYC"


# This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self):
        today = datetime.datetime.now()
        self.search_begin_date = (today + datetime.timedelta(7)).strftime("%d/%m/%Y")
        self.search_end_date = (today + datetime.timedelta(187)).strftime("%d/%m/%Y")
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.max_stopovers = 5
        self.curr = "USD"
        self.fly_from = FLY_FROM_CITY

    # Returns all flight data in a dict
    def get_flight_data(self):
        return {
            "fly_from": self.fly_from,
            "date_from": self.search_begin_date,
            "date_to": self.search_end_date,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "max_stopovers": self.max_stopovers,
            "curr": self.curr,
        }
