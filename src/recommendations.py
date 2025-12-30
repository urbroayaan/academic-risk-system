def recommend_actions(risk_level):
    actions = []

    if risk_level == "Low":
        actions.append("Maintain current study approach")
        actions.append("Periodic review is sufficient")
    elif risk_level == "Medium":
        actions.append("Monitor performance weekly")
        actions.append("Review weaker subjects")
    elif risk_level == "High":
        actions.append("Immediate academic intervention required")
        actions.append("Focus on improving overall average")
        actions.append("Increase support and monitoring")
                           
    return actions