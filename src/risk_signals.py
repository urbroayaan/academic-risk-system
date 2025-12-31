def declining_trend(past_scores):
    if len(past_scores) < 2:
        return 0

    return int(past_scores.iloc[-1] < past_scores.mean())
