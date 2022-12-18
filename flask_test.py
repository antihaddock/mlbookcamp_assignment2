# Test script for checking if the flask app will run locally


import requests
import pandas as pd
import random
import json

# Local port test options
url = 'http://0.0.0.0:3000/classify'

df = pd.read_csv('./Data/test_data.csv')

# This will run through and provide a prediction against each row in the test_data.csv
for i in range(1): 
    # Randomly only return predictions on 5 indexes of the df as the test df has over 10 000 rows still
    index = random.randint(0, len(df))	
    client = df.iloc[index].to_json()
    print(client)
    # response = requests.post(url, json=client)
    # print(response)
    # result = response.json()
    # print(result)