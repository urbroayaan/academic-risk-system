from load_data import load_scores
from risk_signals import declining_trend
from risk_score import total_risk_score
from explanations import risk_level, generate_explanation
from recommendations import recommend_actions
from ml_features import extract_features
from ml_dataset import build_ml_dataset

def main():
    df = load_scores(r"C:\Users\nanda\OneDrive\Desktop\academic-risk-system\data\student_scores.csv")

    for student in df["student"].unique():
        student_data = df[df["student"] == student]
        scores = student_data.sort_values("week")["score"]

        avg_score = scores.mean()
        has_decline = declining_trend(scores)
        risk_score = total_risk_score(has_decline, avg_score)

        level = risk_level(risk_score)
        explanations = generate_explanation(has_decline, avg_score)
        actions = recommend_actions(level)

        print(f"\nStudent: {student}")
        print(f"Average score: {avg_score:.2f}")
        print(f"Risk level: {level}\n")
        print("Explanation: ")
        for reason in explanations:
            print(f"- {reason}")
        print()
        print("Recommended actions: ")
        for action in actions:
            print(f"- {action}")

if __name__ == "__main__":
    main()
