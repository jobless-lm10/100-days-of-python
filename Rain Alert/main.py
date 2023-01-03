import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = os.environ.get("api_key")
MY_LAT = 22.65
My_LONG = 79.65
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

parameters = {
    "lat": MY_LAT,
    "lon": My_LONG,
    "appid": API_KEY,
    "exclude": "minutely,daily,current"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]

umbrella_needed = False
for weather in weather_data[:12]:
    status = weather["weather"][0]["id"]
    if int(status) < 700:
        umbrella_needed = True
        break

if umbrella_needed:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_="+916785492688",
        to=os.environ.get("my_number")
    )
    print(message.status)
