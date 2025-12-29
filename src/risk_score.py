import pandas as pd

def performance_risk(avg_score):
    if avg_score >= 75:
        return 0
    elif avg_score >= 60:
        return 25
    else: return 50

def trend_risk(has_decline):
    if has_decline:
        return 20
    else: return 0

def total_risk_score(has_decline, avg_score):
    return performance_risk(avg_score) + trend_risk(has_decline)