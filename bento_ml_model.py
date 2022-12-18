import bentoml
from bentoml.io import JSON
import pandas as pd

model_ref = bentoml.sklearn.get("stroke_model:latest")

model_runner = model_ref.to_runner()


svc = bentoml.Service("stroke_risk_modelling", runners=[model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(application_data):
    
    #application_data = application_data.to_dict()
    application_data = pd.DataFrame(application_data, index=[0])
    #application_data = pd.read_json(application_data, orient ='index')
    prediction = model_runner.predict.run(application_data)   # Returns a probability score
    
    return {'probability': prediction}