import csv
import random
import argparse
from pathlib import Path


def generate_dataset(rows: int, output_path: str):
    Path("data").mkdir(exist_ok=True)

    with open(output_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "student_id",
            "study_hours",
            "attendance",
            "past_marks",
            "assignment_marks",
            "quiz_marks",
            "result"
        ])

        for i in range(1, rows + 1):
            study_hours = random.uniform(0, 10)
            attendance = random.uniform(30, 100)
            past_marks = random.uniform(0, 100)
            assignment_marks = random.uniform(0, 100)
            quiz_marks = random.uniform(0, 100)

            score = (
                study_hours * 0.9
                + attendance * 0.035
                + past_marks * 0.045
                + assignment_marks * 0.04
                + quiz_marks * 0.035
                - 8.0
            )

            result = "Pass" if score >= 0 else "Fail"

            writer.writerow([
                f"S{i:06d}",
                round(study_hours, 2),
                round(attendance, 2),
                round(past_marks, 2),
                round(assignment_marks, 2),
                round(quiz_marks, 2),
                result
            ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=100000)
    parser.add_argument("--output", type=str, default="data/students.csv")
    args = parser.parse_args()

    generate_dataset(args.rows, args.output)

    print(f"Dataset created: {args.output}")
    print(f"Rows: {args.rows}")