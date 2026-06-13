from benchmark_python import run_python_benchmark
from benchmark_mojo import run_mojo_benchmark
from pathlib import Path


def save_result(text):
    Path("results").mkdir(exist_ok=True)

    with open("results/performance_comparison.txt", "w") as file:
        file.write(text)


def main():
    print("Running Python benchmark...")
    python_time, total_records, python_pass_count = run_python_benchmark()

    print("\nRunning Mojo benchmark...")
    mojo_time, _, mojo_pass_count = run_mojo_benchmark()

    if mojo_time < python_time:
        improvement_text = f"Mojo is {python_time / mojo_time:.2f}x faster than Python"
    else:
        improvement_text = f"Mojo is {mojo_time / python_time:.2f}x slower than Python in this version"

    result = f"""
Performance Test Result
-----------------------
Total records: {total_records}

Original Python calculation completed in: {python_time:.6f} seconds
Mojo calculation completed in: {mojo_time:.6f} seconds

Python predicted pass count: {python_pass_count}
Mojo predicted pass count: {mojo_pass_count}

Result: {improvement_text}

Note:
This first version proves that Python can call Mojo successfully.
However, Mojo is slower here because Python tuple data is converted into Mojo values row by row.
The next improvement is to reduce Python-Mojo conversion overhead.
"""

    print(result)
    save_result(result)


if __name__ == "__main__":
    main()
