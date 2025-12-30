import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from load_data import load_scores
from ml_dataset import build_ml_dataset


def train_on_simulated():
    df = load_scores(r"C:\Users\nanda\OneDrive\Desktop\academic-risk-system\data\student_scores.csv")

    ml_df = build_ml_dataset(df)

    X = ml_df.drop(columns=["label"])
    y = ml_df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred))

    results = X_test.copy()
    results["true_label"] = y_test.values
    results["predicted_probability"] = y_prob

    print("\nSample predictions:")
    print(results.head(10))


if __name__ == "__main__":
    train_on_simulated()