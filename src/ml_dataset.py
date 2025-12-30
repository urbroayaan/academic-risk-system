import pandas as pd
from ml_features import extract_features
from explanations import risk_level
from risk_score import total_risk_score
from risk_signals import declining_trend

def build_ml_dataset(df):
    rows = []

    for student in df["student"].unique():
        student_data = df[df["student"] == student]
        scores = student_data.sort_values("week")["score"]

        avg_score = scores.mean()
        has_decline = declining_trend(scores)
        risk_score = total_risk_score(has_decline, avg_score)

        level = risk_level(risk_score)
        label = 1 if risk_score >= 40 else 0


        features = extract_features(
            scores=scores,
            has_decline=has_decline,
            avg_score=avg_score,
            risk_score=risk_score
        )

        features["label"] = label
        rows.append(features)
    
    return pd.DataFrame(rows)