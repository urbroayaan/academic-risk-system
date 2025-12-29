from load_data import load_scores
from risk_signals import declining_trend

def main():
    df = load_scores(r"C:\Users\student\Desktop\academic-risk-system\data\student_scores.csv")

    for student in df["student"].unique():
        student_data = df[df["student"] == student]
        scores = student_data.sort_values("week")["score"]

        if declining_trend(scores):
            print(f"{student}: Declining performance detected")
        else:
            print(f"{student}: No decline detected")

if __name__ == "__main__":
    main()