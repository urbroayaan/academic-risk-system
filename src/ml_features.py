import pandas as pd

def calculate_volatility(scores):
    scores = pd.Series(scores)
    return scores.std()


def calculate_slope(scores):
    scores = pd.Series(scores)
    if len(scores) < 2:
        return 0

    first = scores.iloc[0]
    last = scores.iloc[-1]
    steps = len(scores) - 1

    return (last - first) / steps


def extract_features(scores, has_decline, avg_score, risk_score):
    scores = pd.Series(scores)
    
    return {
        "avg_score": avg_score,
        "has_decline": int(has_decline),
        "risk_score": risk_score,
        "volatility": calculate_volatility(scores),
        "slope": calculate_slope(scores)
    }