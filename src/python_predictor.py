import csv
from pathlib import Path


def load_records(file_path):
    if not Path(file_path).exists():
        raise FileNotFoundError("Dataset not found. Run generate_dataset.py first.")

    records = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append((
                float(row["study_hours"]),
                float(row["attendance"]),
                float(row["past_marks"]),
                float(row["assignment_marks"]),
                float(row["quiz_marks"])
            ))

    return records


def predict_python(records):
    pass_count = 0

    for row in records:
        score = (
            row[0] * 0.9
            + row[1] * 0.035
            + row[2] * 0.045
            + row[3] * 0.04
            + row[4] * 0.035
            - 8.0
        )

        if score >= 0:
            pass_count += 1

    return pass_count