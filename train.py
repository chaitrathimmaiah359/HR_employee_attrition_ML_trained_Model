import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------------------------
# Step 1: Load Dataset
# -------------------------------------------------

print("Loading dataset...")

df = pd.read_csv("data/employees.csv")

print(df.head())
print(f"\nDataset Shape: {df.shape}")

# -------------------------------------------------
# Step 2: Convert Target Column
# Yes -> 1
# No  -> 0
# -------------------------------------------------

df["left_company"] = df["left_company"].map({
    "Yes": 1,
    "No": 0
})

df["promotion_last_2_years"] = df["promotion_last_2_years"].map({
    "Yes": 1,
    "No": 0
})

# -------------------------------------------------
# Step 3: Convert Categorical Columns
# Department -> One Hot Encoding
# -------------------------------------------------

df = pd.get_dummies(
    df,
    columns=["department"],
    drop_first=True
)

# -------------------------------------------------
# Step 4: Separate Features and Target
# -------------------------------------------------

X = df.drop("left_company", axis=1)

y = df["left_company"]

print("\nFeatures:")
print(X.columns)

# -------------------------------------------------
# Step 5: Split Dataset
# 80% Train
# 20% Test
# -------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"\nTraining Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# -------------------------------------------------
# Step 6: Train Model
# -------------------------------------------------

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complete!")

# -------------------------------------------------
# Step 7: Evaluate Model
# -------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:")
print(f"{accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions
))

# -------------------------------------------------
# Step 8: Save Model
# -------------------------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/employee_model.pkl"
)

print("\nModel saved successfully!")

print("\nLocation:")
print("models/employee_model.pkl")