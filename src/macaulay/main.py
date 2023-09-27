from __future__ import annotations

from typing import TYPE_CHECKING, List

import numpy as np

if TYPE_CHECKING:
    from .typing import MacaulayBracket


def compute(
    equation: List[MacaulayBracket],
    xmin: float = 0.0,
    xmax: float = 1.0,
    n_points: int = 1000,
):
    x = np.linspace(xmin, xmax, n_points, dtype=np.float64)
    y = np.zeros(n_points, dtype=np.float64)
    for element in equation:
        y = np.where(
            x > element["x"],
            y
            + element["coefficient"] * (x - element["x"]) ** element["power"],
            y,
        )
    return np.asarray([x, y]).T


def integrate(equation: List[MacaulayBracket]):
    integrated_equation = []
    for element in equation:
        integrated_equation.append(
            {
                "x": element["x"],
                "coefficient": element["coefficient"] / (element["power"] + 1),
                "power": element["power"] + 1,
            }
        )
    return integrated_equation
