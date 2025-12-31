import pandas as pd
from ml_features import extract_features

def build_ml_dataset(df, cutoff_week=4):
    rows = []

    for student in df["student"].unique():
        student_data = df[df["student"] == student].sort_values("week")

        past = student_data[student_data["week"] <= cutoff_week]
        future = student_data[student_data["week"] > cutoff_week]

        if len(past) < 3 or len(future) < 1:
            continue

        past_scores = past["score"]
        future_scores = future["score"]

        features = extract_features(past_scores)

        label = int(future_scores.mean() < past_scores.mean())

        features["label"] = label
        rows.append(features)

    return pd.DataFrame(rows)
