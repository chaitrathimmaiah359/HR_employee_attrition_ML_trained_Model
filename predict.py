import joblib
import pandas as pd

# -----------------------------
# Step 1: Load trained model
# -----------------------------
model = joblib.load("models/employee_model.pkl")

# -----------------------------
# Step 2: Create a new employee
# -----------------------------
employee = {
    "employee_id": 2001,
    "age": 28,
    "salary": 500000,
    "years_at_company": 2,
    "overtime_hours": 45,
    "work_from_home_days": 2,
    "satisfaction_score": 2,
    "performance_rating": 3,
    "promotion_last_2_years": 0,
    "training_hours": 20,
    "manager_rating": 3,

    # Department One-Hot Encoding
    "department_Finance": 0,
    "department_HR": 0,
    "department_Marketing": 0,
    "department_Sales": 0
}

# -----------------------------
# Step 3: Convert to DataFrame
# -----------------------------
employee_df = pd.DataFrame([employee])

# -----------------------------
# Step 4: Predict
# -----------------------------
prediction = model.predict(employee_df)

probability = model.predict_proba(employee_df)

# -----------------------------
# Step 5: Display Result
# -----------------------------
if prediction[0] == 1:
    print("Prediction : Employee is likely to leave.")
else:
    print("Prediction : Employee is likely to stay.")

print(f"\nProbability of Staying : {probability[0][0]:.2%}")
print(f"Probability of Leaving : {probability[0][1]:.2%}")