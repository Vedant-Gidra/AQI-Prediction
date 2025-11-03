from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('./Models/rf_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    PM25 = float(request.form['PM25'])
    PM10 = float(request.form['PM10'])
    NO2 = float(request.form['NO2'])
    SO2 = float(request.form['SO2'])
    CO = float(request.form['CO'])
    O3 = float(request.form['O3'])

    # Create input array
    features = np.array([[PM25, PM10, NO2, SO2, CO, O3]])
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f'Predicted AQI: {prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
