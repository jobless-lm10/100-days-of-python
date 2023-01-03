import requests
import datetime
import os

GENDER = "MALE"
WEIGHT_KG = "70"
HEIGHT = "171"
AGE = "26"
APP_ID = os.getenv("App_Id")
API_KEY = os.getenv("App_key")
SHEET_API_KEY = os.getenv("Sheet_api_key")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
exercises = response.json()["exercises"]
print(exercises)


sheet_endpoint = "https://api.sheety.co/995c1f44c46de4ca0ce542f85e0c6802/myWorkouts/workouts"
today = datetime.datetime.now()
sheet_header = {
    "Authorization": f"Bearer {SHEET_API_KEY}"
}

for exercise in exercises:
    sheet_params = {
        "workout": {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime('%H:%M:%S'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_header)
    response.raise_for_status()
    print(response.text)