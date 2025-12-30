def risk_level(risk_score):
    if risk_score >= 50:
        return "High"
    elif risk_score >=20:
        return "Medium"
    else: return "Low"

def generate_explanation(has_decline, avg_score):
    explanations = []

    if has_decline:
        explanations.append("Scores are declining over time")
    else:
        explanations.append("No declining trend detected")

    if avg_score < 60:
        explanations.append("Average performance is low")
    else:
        explanations.append("Average performance is stable")

    return explanations
