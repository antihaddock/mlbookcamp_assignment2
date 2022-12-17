# Test script for checking if the flask app will run locally


import requests
import pandas as pd
import random

# Local port test options
url = 'http://0.0.0.0:5000/predict_outcome'



df = pd.read_csv('./Data/test_data.csv')

# This will run through and provide a prediction against each row in the test_data.csv
for i in range(5): # Randomly only return predictions on 5 indexs of the df as the df has over 10 000 rows
    index = random.randint(0, len(df))	
    client = df.iloc[index].to_dict()
    print(client)
    response = requests.post(url, json=client)
    result = response.json()
    print(result)