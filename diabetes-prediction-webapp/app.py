
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('model/diabetes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    input_data = [int(request.form['Pregnancies']),
                  int(request.form['Glucose']),
                  int(request.form['BloodPressure']),
                  int(request.form['SkinThickness']),
                  int(request.form['Insulin']),
                  float(request.form['BMI']),
                  float(request.form['DiabetesPedigreeFunction']),
                  int(request.form['Age'])]

    # Create a DataFrame for the input data
    input_df = pd.DataFrame([input_data], columns=['Pregnancies','Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    # Make prediction
    prediction = model.predict(input_df)

    # Return the prediction result
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)