import time
from typing import Union, Tuple

import numpy as np


def unwrap_matrix(values: np.matrix):
    return values.item(0, 0), values.item(1, 0), values.item(2, 0), values.item(3, 0), values.item(4, 0)


def unwrap_matrix_as_list(values: np.matrix) -> list:
    return [values.item(0, 0), values.item(1, 0), values.item(2, 0), values.item(3, 0), values.item(4, 0)]


def get_values(func_values: Union[list, np.matrix]) -> Tuple[float, float, float, float, float]:
    if type(func_values) is np.matrix:
        return unwrap_matrix(func_values)
    else:
        return func_values[0], func_values[1], func_values[2], func_values[3], func_values[4]


def measure_time(func: callable, *args) -> float:
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


def time_stress(func: callable, logger, iterations: int, *args):
    [logger.log_value("time", measure_time(func, *args)) for _ in range(iterations)]
