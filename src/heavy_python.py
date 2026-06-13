def heavy_compute_python(iterations: int) -> float:
    total = 0.0

    for i in range(iterations):
        x = (i % 1000) * 0.001

        score = (
            x * 0.9
            + (x + 1.0) * 0.035
            + (x + 2.0) * 0.045
            + (x + 3.0) * 0.04
            + (x + 4.0) * 0.035
            - 1.0
        )

        if score >= 0:
            total += score
        else:
            total -= score

    return total
