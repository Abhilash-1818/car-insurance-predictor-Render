from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Category Mappings (as per LabelEncoder)
job_map = {
    "management": 0,
    "blue-collar": 1,
    "student": 2,
    "technician": 3,
    "admin.": 4,
    "services": 5,
    "self-employed": 6,
    "entrepreneur": 7,
    "retired": 8,
    "unemployed": 9,
    "housemaid": 10,
    "unknown": 11
}

marital_map = {
    "single": 0,
    "married": 1,
    "divorced": 2
}

education_map = {
    "primary": 0,
    "secondary": 1,
    "tertiary": 2,
    "unknown": 3
}

communication_map = {
    "telephone": 0,
    "cellular": 1
}

month_map = {
    "jan": 0, "feb": 1, "mar": 2, "apr": 3,
    "may": 4, "jun": 5, "jul": 6, "aug": 7,
    "sep": 8, "oct": 9, "nov": 10, "dec": 11
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        age = int(request.form['Age'])
        job = job_map[request.form['Job']]
        marital = marital_map[request.form['Marital']]
        education = education_map[request.form['Education']]
        balance = int(request.form['Balance'])
        hhinsurance = int(request.form['HHInsurance'])
        carloan = int(request.form['CarLoan'])
        communication = communication_map[request.form['Communication']]
        day = int(request.form['LastContactDay'])
        month = month_map[request.form['LastContactMonth']]
        contacts = int(request.form['NoOfContacts'])
        dayspassed = int(request.form['DaysPassed'])
        prevattempts = int(request.form['PrevAttempts'])

        # Combine all inputs
        features = np.array([[age, job, marital, education, balance,
                              hhinsurance, carloan, communication, day,
                              month, contacts, dayspassed, prevattempts]])

        # Scale input
        scaled_features = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled_features)[0]
        result = "This person is likely to buy car insurance." if prediction == 1 else "This person is NOT likely to buy car insurance."

        return render_template('index.html', prediction_text=f"Prediction: {result}")

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)