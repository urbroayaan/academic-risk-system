def risk_level(risk_score):
    if risk_score >= 50:
        return "High"
    elif risk_score >=20:
        return "Medium"
    else: return "Low"