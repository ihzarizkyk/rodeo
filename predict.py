from flask import Flask, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

predict = Flask(__name__)

# Load the model
model = DecisionTreeClassifier()
model.load("accident_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.get_json()
    
    # Make a prediction using the model
    prediction = model.predict([data])
    
    # Return the prediction to the client
    return str(prediction[0])

if __name__ == "__main__":
    app.run()
