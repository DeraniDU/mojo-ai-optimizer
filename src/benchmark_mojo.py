from time import perf_counter

import mojo.importer
import score_ops

from python_predictor import load_records


DATASET_PATH = "data/students.csv"


def run_mojo_benchmark():
    records = load_records(DATASET_PATH)

    start = perf_counter()
    pass_count = score_ops.batch_predict_count_mojo(records)
    end = perf_counter()

    mojo_time = end - start

    print("Mojo Benchmark Result")
    print("---------------------")
    print(f"Total records: {len(records)}")
    print(f"Predicted pass count: {pass_count}")
    print(f"Optimized Mojo calculation completed in: {mojo_time:.6f} seconds")

    return mojo_time, len(records), int(pass_count)


if __name__ == "__main__":
    run_mojo_benchmark()