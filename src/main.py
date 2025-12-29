from load_data import load_scores
from risk_signals import declining_trend
from risk_score import total_risk_score

def main():
    df = load_scores(r"C:\Users\student\Desktop\academic-risk-system\data\student_scores.csv")

    for student in df["student"].unique():
        student_data = df[df["student"] == student]
        scores = student_data.sort_values("week")["score"]
        avg_score = scores.mean()
        has_decline = declining_trend(scores)

        print(f"\nStudent: {student}")

        if has_decline:
            print(f"Decline detected: Yes")
        else: print(f"Decline detected: No")

        print(f"Average score: {avg_score:.2f}")
        print(f"Risk score: {total_risk_score(has_decline, avg_score)}")

if __name__ == "__main__":
    main()
