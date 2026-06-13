from time import perf_counter

from python_predictor import load_records, predict_python

try:
    import mojo.importer  # type: ignore
    import score_ops
except ModuleNotFoundError:
    mojo = None
    score_ops = None


DATASET_PATH = "data/students.csv"


def run_mojo_benchmark():
    records = load_records(DATASET_PATH)

    start = perf_counter()
    if score_ops is not None:
        pass_count = score_ops.batch_predict_count_mojo(records)
        backend_name = "Mojo"
    else:
        pass_count = predict_python(records)
        backend_name = "Python fallback"
    end = perf_counter()

    mojo_time = end - start

    print("Mojo Benchmark Result")
    print("---------------------")
    print(f"Total records: {len(records)}")
    print(f"Predicted pass count: {pass_count}")
    print(f"{backend_name} calculation completed in: {mojo_time:.6f} seconds")

    if score_ops is None:
        print("Mojo runtime not available; used the Python implementation instead.")

    return mojo_time, len(records), int(pass_count)


if __name__ == "__main__":
    run_mojo_benchmark()