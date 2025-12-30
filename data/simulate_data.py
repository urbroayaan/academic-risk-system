import random
import pandas as pd

def simulate_student(student_id, pattern, weeks=6):
    scores = []

    if pattern == "high_stable":
        base = random.randint(80, 90)
        for _ in range(weeks):
            scores.append(base + random.randint(-3, 3))

    elif pattern == "declining":
        base = random.randint(75, 85)
        for i in range(weeks):
            scores.append(base - i * random.randint(2, 4))

    elif pattern == "volatile":
        base = random.randint(65, 85)
        for _ in range(weeks):
            scores.append(base + random.randint(-20, 20))

    elif pattern == "low":
        base = random.randint(45, 60)
        for _ in range(weeks):
            scores.append(base + random.randint(-3, 3))

    rows = []
    for week, score in enumerate(scores, start=1):
        rows.append({
            "student": student_id,
            "week": week,
            "score": max(0, min(100, score))
        })

    return rows


def generate_dataset(num_students=1000):
    patterns = ["high_stable", "declining", "volatile", "low"]
    data = []

    for i in range(num_students):
        student_id = f"S_{i}"
        pattern = random.choice(patterns)
        data.extend(simulate_student(student_id, pattern))

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_dataset(2000)
    df.to_csv(r"C:\Users\nanda\OneDrive\Desktop\academic-risk-system\data\student_scores.csv", index=False)
    print("Simulated dataset saved.")
