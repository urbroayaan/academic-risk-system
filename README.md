# Academic Risk Prediction System (Rule-Based + ML)

A hybrid decision intelligence system that detects, explains, and predicts academic risk using a combination of rule-based logic and machine learning.

---

## 🔍 Problem Statement

Students often show early warning signs of academic risk such as:
- declining performance trends
- unstable (volatile) scores
- consistently low averages

Traditional systems either rely on static thresholds or black-box ML models that lack explainability.

This project addresses that gap by building:
- an explainable rule-based risk engine
- a scalable ML prediction layer
- actionable recommendations

---

## 🧠 System Architecture

Raw Scores
↓
Feature Engineering
↓
Rule-Based Risk Scoring
↓
Risk Level + Explanation
↓
Recommended Actions
↓
ML Risk Probability (Future Risk)


---

## ⚙️ Features

### Rule-Based Engine
- Detects declining trends
- Computes performance-based risk
- Assigns Low / Medium / High risk
- Generates human-readable explanations
- Provides intervention recommendations

### Machine Learning Layer
- Engineered features:
  - average score
  - trend direction
  - volatility (score instability)
  - slope (rate of change)
- Logistic Regression model
- Outputs probability of becoming high-risk
- Designed to integrate with rule engine

---

## 📊 Data Strategy

- Supports real CSV student score data
- Includes realistic data simulation engine for large-scale ML training
- Labels derived from domain logic (weak supervision)

---

## 🧪 Technologies Used

- Python
- pandas
- scikit-learn
- rule-based decision logic
- synthetic data simulation

---

## 🚀 How to Run

### Rule-Based System

python src/main.py
Train ML Model
python src/train_simulated_model.py

📌 Key Learnings
Importance of feature engineering before ML

Hybrid systems outperform pure rule-based or pure ML approaches

Explainability is critical in risk-sensitive domains

Synthetic data is useful for validating ML pipelines

📈 Future Work
Remove label leakage and improve generalization

Add feature importance analysis

Integrate ML probabilities into decision engine

Build visualization dashboard

👤 Author
Built as a learning-focused, end-to-end decision intelligence system demonstrating real-world ML engineering practices.


---
