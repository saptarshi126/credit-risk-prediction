import joblib
import pandas as pd

# Load trained model
model = joblib.load("credit_risk_prediction/models/credit_model.pkl")

print("\n=== Credit Risk Prediction ===\n")

# Take user input
age = int(input("Enter Age: "))
credit_amount = float(input("Enter Credit Amount: "))
duration = int(input("Enter Loan Duration (months): "))
employment = int(input("Employment (1=Employed, 0=Unemployed): "))
savings = int(input("Savings (0=Low, 1=Medium, 2=High): "))

# Create DataFrame
input_data = pd.DataFrame(
    [[age, credit_amount, duration, employment, savings]],
    columns=["age", "credit_amount", "duration", "employment", "savings"]
)

# Predict
prediction = model.predict(input_data)[0]

# Output result
if prediction == 1:
    print("\n✅ Low Credit Risk")
else:
    print("\n❌ High Credit Risk")
