import pandas as pd

def calculate_volatility(scores):
    scores = pd.Series(scores)
    return scores.std()

def calculate_slope(scores):
    scores = pd.Series(scores)
    if len(scores) < 2:
        return 0

    return (scores.iloc[-1] - scores.iloc[0]) / (len(scores) - 1)

def extract_features(past_scores):
    past_scores = pd.Series(past_scores)

    return {
        "avg_score": past_scores.mean(),
        "volatility": calculate_volatility(past_scores),
        "slope": calculate_slope(past_scores),
    }
