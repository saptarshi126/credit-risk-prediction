🔍 Project Overview
This project is an end-to-end Machine Learning application that predicts whether a customer is a high credit risk or low credit risk based on financial and personal attributes.
The model can help financial institutions make data-driven loan approval decisions.

The project covers the complete ML workflow — from data loading and model training to saving the model and using it for real-time predictions via a CLI application.

🧠 Problem Statement
Banks and financial institutions face significant losses due to loan defaults.
The goal of this project is to predict credit risk using historical customer data and classify applicants as:
✅ Low Credit Risk
❌ High Credit Risk

🗂 Dataset Description

The dataset contains the following features:
Feature	Description
age	            Age of the applicant
credit_amount	Loan amount requested
duration	    Loan duration (months)
employment	    Employment status (1 = Employed, 0 = Unemployed)
savings	        Savings level (0 = Low, 1 = Medium, 2 = High)
credit_risk	    Target variable (1 = Low Risk, 0 = High Risk)

📁 Dataset location:
dataset/credit_data.csv

⚙️ Tech Stack & Tools
Python
Pandas
NumPy
Scikit-learn
Joblib
VS Code
Virtual Environment (venv)

🤖 Machine Learning Approach
Model Used: Logistic Regression
Reason: Logistic Regression is widely used in financial risk modeling due to its simplicity, efficiency, and interpretability.
Train-Test Split: 80% training, 20% testing
Evaluation Metric: Accuracy Score

📈 Model Performance
Model Accuracy: 1.0

How to Run the Project
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd credit_risk_prediction
2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Train the Model
python credit_risk_prediction/train_model.py
5️⃣ Run the Prediction App
python credit_risk_prediction/app.py


Sample Input & Output

Input:
Age: 30
Credit Amount: 6000
Loan Duration: 12
Employment: 1
Savings: 1

Output:
✅ Low Credit Risk

📁 Project Structure
credit_risk_prediction/
│
├── credit_risk_prediction/
│   ├── train_model.py
│   ├── app.py
│   ├── models/
│   │   └── credit_model.pkl
│   ├── README.md
│
├── dataset/
│   └── credit_data.csv
│
├── venv/
└── requirements.txt

🔮 Future Improvements
Use a larger and real-world dataset
Try advanced models (Random Forest, XGBoost)
Add model evaluation metrics like precision, recall, ROC-AUC
Build a Flask-based web interface
Deploy the model as an API

👤 Author
Saptarshi Kundu
B.Tech CSE (AIML)
Manipal University Jaipur

⭐ Final Note
This project demonstrates practical Machine Learning skills, real-world debugging, and an end-to-end workflow.

