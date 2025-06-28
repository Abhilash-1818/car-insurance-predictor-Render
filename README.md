# 🚗 Car Insurance Subscription Predictor

A machine learning web application that predicts whether a customer is likely to subscribe to car insurance based on their profile. Built using **Flask**, **scikit-learn**, and **Render** for deployment.

---

## 📊 Dataset Information

The model is trained on a marketing dataset with customer information such as:
- Age, Job, Marital Status, Education
- Balance, Car Loan, HH Insurance
- Contact type, Month, Number of previous attempts, etc.

The target variable is:
- `CarInsurance` (1 = Subscribed, 0 = Not Subscribed)

---

## 🧠 Technologies Used

- Python
- Flask (for backend API)
- HTML (frontend form)
- scikit-learn (Random Forest model)
- imbalanced-learn (SMOTE balancing)
- MinMaxScaler (feature scaling)
- Render (deployment)
- Git & GitHub (version control)

---

## ⚙️ How It Works

1. User inputs data through a simple HTML form (dropdowns & numbers)
2. Flask backend collects the input and:
   - Maps text labels (e.g. `"married"`) to numeric values
   - Scales features using `MinMaxScaler`
   - Predicts the result using a trained `RandomForestClassifier`
3. The prediction (`Subscribed` or `Not Subscribed`) is displayed on the same page

---
## 🌐 Live Application

🚀 Try the app here: [Click to Open Car Insurance Predictor](https://car-insurance-predictor-render.onrender.com)

> 📌 Deployed using **Render** and always accessible online
