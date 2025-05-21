import requests
import time
import random

API_URL = "http://api:80/predict"

while True:
    x = random.uniform(0, 100)
    try:
        response = requests.post(API_URL, json={"x": x})
        print(f"Sent: {x:.2f}, Got: {response.json()}")
    except Exception as e:
        print("Error sending request:", e)
    time.sleep(1)
