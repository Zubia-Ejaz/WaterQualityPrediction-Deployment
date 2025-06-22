from flask import Flask, render_template, request, redirect
import joblib
import numpy as np
import csv
from datetime import datetime
import uuid

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html', prediction=None, success=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(f)) for f in [
            'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
            'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'
        ]]
        scaled_features = scaler.transform([features])
        prediction = model.predict(scaled_features)[0]
        result = "✅ Water is Safe for Drinking" if prediction == 1 else "❌ Water is Not Safe for Drinking"
        return render_template('index.html', prediction=result, success=None)
    except Exception as e:
        return render_template('index.html', prediction=None, success=f"Error: {e}")

@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form.get('name')
    suggestion = request.form.get('suggestion')
    feedback_type = request.form.get('type')
    date = datetime.now().strftime('%Y-%m-%d')
    version = "v1.0"
    user_id = str(uuid.uuid4())

    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([user_id, name, suggestion, feedback_type, date, version])

    return render_template('index.html', prediction=None, success="✅ Thank you for your feedback!")

if __name__ == '__main__':
    app.run(debug=True)
