import numpy as np

MAXIMUM_ITERATIONS = 100

R_1, R_5, R_6, R_7, R_8, R_9, R_10 = np.float64(10), np.float64(0.193), np.float64(4.10622 * 1e-4), \
                                     np.float64(5.45177 * 1e-4), np.float64(4.4975 * 1e-7), \
                                     np.float64(3.40735 * 1e-5), np.float64(9.615 * 1e-7)


def exercise_function(func_values: list) -> list:
    x_1, x_2, x_3, x_4, x_5 = func_values
    first_function = x_1 * x_2 + x_1 - 3 * x_5
    second_function = 2 * x_1 * x_2 + x_1 + 3 * R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 \
                      + R_9 * x_2 * x_4 + R_8 * x_2 - R_1 * x_5
    third_function = 2 * x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + 2 * R_5 * x_3 ** 2 + R_6 * x_3 \
                     - 8 * np.float64(x_5)  # aqui
    fourth_function = R_9 * x_2 * x_4 + 2 * x_4 ** 2 - 4 * R_1 * x_5
    fifth_function = x_1 * x_2 + x_1 + R_10 * x_2 ** 2 + x_2 * x_3 ** 2 + R_7 * x_2 * x_3 + R_9 * x_2 * x_4 \
                     + R_8 * x_2 + R_5 * x_3 ** 2 + R_6 * x_3 + x_4 ** 2 - 1  # aqui
    return [first_function, second_function, third_function, fourth_function, fifth_function]


def jacobian_of_function(func_values: np.matrix):
    x_1, x_2, x_3, x_4, x_5 = func_values
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


def get_answer():
    return [3.43023016e-03, 3.13264968e+01, 6.83504014e-02, 8.59528996e-01, 3.69624414e-02]


def newton(x: list, function: callable, jacobian: callable, tolerance: float):
    for i in range(int(MAXIMUM_ITERATIONS)):
        f_of_x = function(x)
        jacobian_of_x = jacobian(x)
        y_increment = -np.linalg.solve(jacobian_of_x, f_of_x)
        x = x + y_increment
        increment_norm = np.linalg.norm(y_increment)
        if increment_norm < tolerance:
            print(f"A função convergiu com sucesso em {i + 1} iterações..")
            return x
    raise RuntimeError("Função não convergiu.")


def _main():
    x_0 = [10., 10., 10., 10., 10.]
    result = newton(x_0, exercise_function, jacobian_of_function, 1e-10)
    print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {result}.")


if __name__ == '__main__':
    _main()
