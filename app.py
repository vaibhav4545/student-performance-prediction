from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("C:/Users/Admin/OneDrive/Desktop/Documents/student-prediction-analysis/model/model.pkl")

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        previous_score = float(request.form['previous_score'])
        sleep_hours = float(request.form['sleep_hours'])

        # Prepare input
        features = np.array([[study_hours, attendance, previous_score, sleep_hours]])

        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"Predicted Score: {prediction:.2f}")

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)