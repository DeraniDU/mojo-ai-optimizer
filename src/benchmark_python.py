from time import perf_counter
from python_predictor import load_records, predict_python


DATASET_PATH = "data/students.csv"


def run_python_benchmark():
    records = load_records(DATASET_PATH)

    start = perf_counter()
    pass_count = predict_python(records)
    end = perf_counter()

    python_time = end - start

    print("Python Benchmark Result")
    print("-----------------------")
    print(f"Total records: {len(records)}")
    print(f"Predicted pass count: {pass_count}")
    print(f"Original Python calculation completed in: {python_time:.6f} seconds")

    return python_time, len(records), pass_count


if __name__ == "__main__":
    run_python_benchmark()