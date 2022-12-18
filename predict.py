import pickle
import pandas as pd
from flask import Flask, request, jsonify

with open('./Models/stroke-prediction.bin', 'rb') as f_in:
    model = pickle.load(f_in)



# Define a function we can use in the server which takes in data, transforms the data and returns a class and probability
def predict_outcome(X, model):
    X = pd.DataFrame(X, index=[0])
    y_pred = model.predict(X)
    y_pred_prob = model.predict_proba(X)
    
    return y_pred, y_pred_prob 

app = Flask('classify')


@app.route('/predict_outcome', methods=['POST'])
def predict_outcomes():
    data = request.get_json()
    prediction, prediction_prob = predict_outcome(data, model)
    
    result = {
        'Class': prediction.tolist(),
        'probability': prediction_prob.tolist()
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)