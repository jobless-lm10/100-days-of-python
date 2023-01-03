import os
import time

import requests
import datetime
import smtplib

MY_LAT = 22.600599
MY_LONG = 79.611099
MY_TIME_DIFF = datetime.time(hour=5, minute=30)
MY_EMAIL = os.environ.get("my_email")
MY_PASSWORD = os.environ.get("password")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]

    longitude = float(data["longitude"])
    latitude = float(data["latitude"])
    # print(f"Latitude = {latitude}, longitude = {longitude}")
    return abs(latitude - MY_LAT) <= 5 and abs(longitude - MY_LONG) <= 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = datetime.time.fromisoformat(data["sunrise"].split("T")[1][:5])
    sunrise = datetime.time(sunrise.hour + MY_TIME_DIFF.hour, sunrise.minute + MY_TIME_DIFF.minute)
    sunset = datetime.time.fromisoformat(data["sunset"].split("T")[1][:5])
    sunset = datetime.time(sunset.hour + MY_TIME_DIFF.hour, sunset.minute + MY_TIME_DIFF.minute)
    now = datetime.datetime.now()
    now = datetime.time(hour=now.hour, minute=now.minute)

    return now > sunset or now < sunrise


while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
    time.sleep(300)
