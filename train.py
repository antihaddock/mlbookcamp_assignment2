import pandas as pd
#import pickle
import bentoml

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Read in data
df = pd.read_csv('./Data/health_data.csv')

# -------------- Test Train split and create numeric target variable ------------------

# Split data into X & Y
y = df['Stroke']
X = df.drop(columns=['Stroke', 'Diabetes', 'Hypertension'])


# Split into test and train at 70/30
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=1)

# now split into train and validation to give 60/20/20 split
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.5, random_state=42)

# ------------------  Train a Classification Tree Model --------------------------------------------------------- 
model = DecisionTreeClassifier()
model.fit(X, y)

# ------------- Export trained model to pickle file -------------------------------------------------------

# with open('./Models/stroke-prediction.bin', 'wb') as f_out:
#     pickle.dump(model, f_out)


#---------------- Save model with BentoML -------------------------------------------------------------------
saved_model = bentoml.sklearn.save_model("Stroke_Model", model)
print(f"Model saved: {saved_model}")