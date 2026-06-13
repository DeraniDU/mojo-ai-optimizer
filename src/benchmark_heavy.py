from time import perf_counter

import mojo.importer
import heavy_ops

from heavy_python import heavy_compute_python


def main():
    iterations = 5_000_000

    print("Heavy AI-Style Calculation Benchmark")
    print("------------------------------------")
    print(f"Iterations: {iterations}")

    start = perf_counter()
    python_result = heavy_compute_python(iterations)
    python_time = perf_counter() - start

    start = perf_counter()
    mojo_result = heavy_ops.heavy_compute_mojo(iterations)
    mojo_time = perf_counter() - start

    print("\nPython Result")
    print("-------------")
    print(f"Result value: {python_result:.4f}")
    print(f"Python time: {python_time:.6f} seconds")

    print("\nMojo Result")
    print("-----------")
    print(f"Result value: {float(mojo_result):.4f}")
    print(f"Mojo time: {mojo_time:.6f} seconds")

    print("\nPerformance Comparison")
    print("----------------------")

    if mojo_time < python_time:
        print(f"Mojo is {python_time / mojo_time:.2f}x faster than Python")
    else:
        print(f"Mojo is {mojo_time / python_time:.2f}x slower than Python")


if __name__ == "__main__":
    main()
