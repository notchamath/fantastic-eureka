import os
from twilio.rest import Client

# Twilio Config
TWILIO_KEY = os.environ["TWILIO_KEY"]
account_sid = "ACe6fdb96386238b8f80893e15bc457b7a"


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, TWILIO_KEY)

    def send_text(self, flight):

        dep_date = flight["local_departure"].split("T")[0]
        text = (
            "Low Price Alert! "
            f"Seats remaining: {flight['availability']['seats']}.\n"
            f"Only ${flight['price']} to fly from "
            f"{flight['cityFrom']}-{flight['flyFrom']} to "
            f"{flight['cityTo']}-{flight['flyTo']}, for "
            f"{flight['nightsInDest']} nights from {dep_date}.\n"
            f"Link: {flight['deep_link']}"
        )

        message = self.client.messages.create(
            to="+16466629576",
            from_="+18446480994",
            body=text
        )

        print(message.status)
