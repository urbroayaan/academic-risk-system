import pandas

def declining_trend(scores):
    return scores.iloc[-1] < scores.iloc[0]


