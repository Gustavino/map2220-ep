from enum import Enum
from typing import Union, List

import numpy as np

from utils.utils import get_values, unwrap_matrix_as_list

MAXIMUM_ITERATIONS = 1000

R_1, R_5, R_6, R_7, R_8, R_9, R_10 = np.float64(10), np.float64(0.193), np.float64(4.10622 * 1e-4), \
    np.float64(5.45177 * 1e-4), np.float64(4.4975 * 1e-7), \
    np.float64(3.40735 * 1e-5), np.float64(9.615 * 1e-7)

OPTIMAL_BROYDEN_MAXIMUM = 44
OPTIMAL_BROYDEN_MINIMUM = 2.71e-3

OPTIMAL_BROYDEN_FIRST_ORDER_MAXIMUM = 42
OPTIMAL_BROYDEN_FIRST_ORDER_MINIMUM = 2.71e-3

OPTIMAL_BROYDEN_SECOND_ORDER_MAXIMUM = 42
OPTIMAL_BROYDEN_SECOND_ORDER_MINIMUM = 2.71e-3


class CommonKeys:
    time = "time"


class NewtonLoggerKeys(CommonKeys):
    x = "newton_x"
    norm_of_x = "norm of x"
    increment = "increment"
    increment_norm = "increment_norm"
    residual = "residual"
    residual_norm = "residual_norm"
    number_of_iterations = "number_of_iterations"


# todo: maybe move to broyden utils
class BroydenLoggerKeys(CommonKeys):
    x = "broyden_x"
    norm_of_x = "norm of x"
    increment = "increment"
    increment_norm = "increment_norm"
    residual = "residual"
    residual_norm = "residual_norm"
    number_of_iterations = "number_of_iterations"


class Order(Enum):
    FIRST = 1
    SECOND = 2


def exercise_function(func_values: Union[list, np.matrix]) -> list:
    x_1, x_2, x_3, x_4, x_5 = get_values(func_values)
    first_function = x_1 * x_2 + x_1 - 3 * x_5
    second_function = 2 * x_1 * x_2 + x_1 + 3 * R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + R_9 * x_2 * x_4 + R_8 * x_2 - R_1 * x_5
    third_function = 2 * x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + 2 * R_5 * x_3 ** 2 + R_6 * x_3 - 8 * np.float64(x_5)
    fourth_function = R_9 * x_2 * x_4 + 2 * x_4 ** 2 - 4 * R_1 * x_5
    fifth_function = x_1 * x_2 + x_1 + R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + R_9 * x_2 * x_4 \
                     + R_8 * x_2 + R_5 * x_3 ** 2 + R_6 * x_3 + x_4 ** 2 - 1
    return [first_function, second_function, third_function, fourth_function, fifth_function]


def jacobian_of_exercise_function(func_values: np.matrix):
    x_1, x_2, x_3, x_4, x_5 = get_values(func_values)
    return [
        [x_2 + 1, x_1, 0, 0, -3],
        [2 * x_2 + 1, 2 * x_1 + 6 * R_10 * x_2 + x_3 ** 2 + R_7 * x_3 + R_9 * x_4 + R_8, 2 * x_2 * x_3 + R_7 * x_2, R_9 * x_2, -R_1],
        [0, 2 * x_3 ** 2 + R_7 * x_3, 4 * x_2 * x_3 + R_7 * x_2 + 4 * R_5 * x_3 + R_6, 0, -8.],
        [0, R_9 * x_4, 0, R_9 * x_2 + 4 * x_4, -4 * R_1],
        [x_2 + 1, x_1 + 2 * R_10 * x_2 + x_3 ** 2 + R_7 * x_3 + R_9 * x_4 + R_8,
         2 * x_2 * x_3 + R_7 * x_2 + 2 * R_5 * x_3 + R_6, R_9 * x_2 + 2 * x_4, 0.]
    ]


def jacobian_with_finite_differences(function: callable, order: Order, step_size: float, func_values: Union[List[float], np.matrix]):
    def forward_differences():
        return (function(values + indicator * step_size)[row] - function(values)[row]) / step_size

    def centered_differences():
        return (function(values + indicator * step_size)[row] - function(
            values - indicator * step_size)[row]) / (2 * step_size)

    values = func_values if not type(func_values) is np.matrix else unwrap_matrix_as_list(func_values)
    calculate_derivative = forward_differences if order == Order.FIRST else centered_differences

    num_of_columns = len(values)
    num_of_rows = len(function(values))

    jacobian = np.zeros(num_of_rows * num_of_columns).reshape(num_of_rows, num_of_columns)
    for row in range(num_of_rows):
        for column in range(num_of_columns):
            indicator = np.zeros(num_of_columns)
            indicator[column] = 1
            jacobian[row][column] = calculate_derivative()

    return jacobian
