import numpy as np
from .matrix import draw_figure


def run_sequence(X, steps, title):
    current = X.copy()
    total_matrix = np.eye(2)

    for step_number, (name, transform, parameters, matrix) in enumerate(
        steps, start=1
    ):
        previous = current.copy()
        print("parameters:", parameters)
        current = transform(current, *parameters)

        total_matrix = matrix @ total_matrix

        draw_figure(
            previous,
            current,
            f"{name}",
            f"{title}: step {step_number} - {name}"
        )

    print(f"\n{title} - total matrix:")
    print(total_matrix)

    draw_figure(X, current, f"{title}: final result")

    return current