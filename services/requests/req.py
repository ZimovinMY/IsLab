import requests
import time
import random

for i in range(50):
    params = {'id': i}
    data = {
        "Car_Name": "Toyota Corolla",
        ##"Year": random.randint(1980,2024),
        "Selling_Price": random.randint(1,20),
        "Driven_kms": random.randint(0,100000),
        "Fuel_Type": "Petrol",
        "Selling_type": "Dealer",
        "Transmission": "Manual",
        "Owner": random.randint(0,10)
    }
    response = requests.post('http://price-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())