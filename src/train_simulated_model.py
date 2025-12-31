from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from load_data import load_scores
from ml_dataset import build_ml_dataset

def train_on_simulated():
    df = load_scores("data/student_scores.csv")

    ml_df = build_ml_dataset(df)

    X = ml_df.drop(columns=["label"])
    y = ml_df["label"]

    split = int(0.75 * len(ml_df))
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    train_on_simulated()
