#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
import os
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = os.environ.get("email")
MY_PASSWORD = os.environ.get("password")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {}
for (index, data_row) in data.iterrows():
    if (data_row["month"], data_row["day"]) not in birthdays_dict:
        birthdays_dict[(data_row["month"], data_row["day"])] = [data_row]
    else:
        birthdays_dict[(data_row["month"], data_row["day"])] += [data_row]

if today_tuple in birthdays_dict:
    for person in birthdays_dict[today_tuple]:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
