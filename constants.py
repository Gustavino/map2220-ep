from typing import Union

import numpy as np

from utils.utils import get_values

MAXIMUM_ITERATIONS = 100

R_1, R_5, R_6, R_7, R_8, R_9, R_10 = np.float64(10), np.float64(0.193), np.float64(4.10622 * 1e-4), \
                                     np.float64(5.45177 * 1e-4), np.float64(4.4975 * 1e-7), \
                                     np.float64(3.40735 * 1e-5), np.float64(9.615 * 1e-7)


class NewtonLoggerKeys:
    time = "time"
    x = "x"
    norm_of_x = "norm of x"
    increment = "increment"
    increment_norm = "increment_norm"
    residual = "residual"
    residual_norm = "residual_norm"


class BroydenLoggerKeys:
    time = "time"


def exercise_function(func_values: Union[list, np.matrix]) -> list:
    x_1, x_2, x_3, x_4, x_5 = get_values(func_values)
    first_function = x_1 * x_2 + x_1 - 3 * x_5
    second_function = 2 * x_1 * x_2 + x_1 + 3 * R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 \
                      + R_9 * x_2 * x_4 + R_8 * x_2 - R_1 * x_5
    third_function = 2 * x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + 2 * R_5 * x_3 ** 2 + R_6 * x_3 \
                     - 8 * np.float64(x_5)  # aqui
    fourth_function = R_9 * x_2 * x_4 + 2 * x_4 ** 2 - 4 * R_1 * x_5
    fifth_function = x_1 * x_2 + x_1 + R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + R_9 * x_2 * x_4 \
                     + R_8 * x_2 + R_5 * x_3 ** 2 + R_6 * x_3 + x_4 ** 2 - 1  # aqui
    return [first_function, second_function, third_function, fourth_function, fifth_function]


def jacobian_of_exercise_function(func_values: np.matrix):
    x_1, x_2, x_3, x_4, x_5 = get_values(func_values)
    return [
        [x_2 + 1, x_1, 0, 0, -3],
        [2 * x_2 + 1,
         2 * x_1 + 6 * R_10 * x_2 + x_3 ** 2 + R_7 * x_3 + R_9 * x_4 + R_8,
         2 * x_2 * x_3 + R_7 * x_2,
         R_9 * x_2, -R_1],
        [0, 2 * x_3 ** 2 + R_7 * x_3, 4 * x_2 * x_3 + R_7 * x_2 + 4 * R_5 * x_3 + R_6, 0, -8.],  # aqui
        [0, R_9 * x_4, 0, R_9 * x_2 + 4 * x_4, -4 * R_1],  # aqui
        [x_2 + 1, x_1 + 2 * R_10 * x_2 + x_3 ** 2 + R_7 * x_3 + R_9 * x_4 + R_8,
         2 * x_2 * x_3 + R_7 * x_2 + 2 * R_5 * x_3 + R_6, R_9 * x_2 + 2 * x_4, 0.]
    ]
