import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
endpoint = os.environ['endpoint']

text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": text,
    "gender": "female",
    "weight_kg": 50,
    "height_cm": 156,
    "age": 30
}

response = requests.post(endpoint, data=parameters, headers=headers)
result = response.json()

url = os.environ['url']
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
token = os.environ['token']
my_headers = {
    "Authorization": f"Basic {token}",
}

for exercise in result["exercises"]:

    inputs = {
          "workout": {
               "date": date,
               "time": time,
               "exercise": exercise["name"].title(),
               "duration": exercise["duration_min"],
               "calories": exercise["nf_calories"]
                     }
            }
    
    response = requests.post(url, json=inputs, headers=my_headers)
    print(response.json())


