import datetime


# This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self):
        today = datetime.datetime.now()
        self.search_begin_date = (today + datetime.timedelta(7)).strftime("%d/%m/%Y")
        self.search_end_date = (today + datetime.timedelta(187)).strftime("%d/%m/%Y")
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = "USD"

