from pprint import pprint

import numpy as np

from constants import MAXIMUM_ITERATIONS, exercise_function, jacobian_of_exercise_function, NewtonLoggerKeys, \
    BroydenLoggerKeys
from utils.Logger import Logger
from utils.Plotter import Plotter
from utils.utils import time_stress


def newton(x: list, function: callable, jacobian: callable, tolerance: float, logger: Logger):
    def add_residual(new_f_of_x):
        if i > 0:
            logger.log_value(NewtonLoggerKeys.residual, new_f_of_x)
            logger.log_value(NewtonLoggerKeys.residual_norm, np.linalg.norm(new_f_of_x, -np.inf))

    for i in range(int(MAXIMUM_ITERATIONS)):
        f_of_x = function(x)
        add_residual(f_of_x)

        logger.log_value(NewtonLoggerKeys.x, x)
        logger.log_value(NewtonLoggerKeys.norm_of_x, np.linalg.norm(x, -np.inf))

        jacobian_of_x = jacobian(x)
        y_increment = -np.linalg.solve(jacobian_of_x, f_of_x)
        x = x + y_increment
        increment_norm = np.linalg.norm(y_increment)

        logger.log_value(NewtonLoggerKeys.increment, y_increment)
        logger.log_value(NewtonLoggerKeys.increment_norm, np.linalg.norm(y_increment, -np.inf))

        if increment_norm < tolerance:
            print(f"A função convergiu com sucesso em {i + 1} iterações.")
            return x
    raise RuntimeError("Função não convergiu.")


def broyden(x_0: np.matrix, function: callable, jacobian: callable, tolerance: float):
    a_0 = np.matrix(jacobian(x_0))
    v: np.matrix = np.matrix(function(x_0)).T
    A = np.linalg.inv(a_0)
    s = -A @ v
    approximate_solution = x_0 + s
    for i in range(int(MAXIMUM_ITERATIONS) - 1):
        w = v
        v = np.matrix(function(approximate_solution)).T
        y = v - w
        z = -A @ y
        p = -s.T @ z
        u_transposed = s.T @ A
        A = A + (1 / p.item(0, 0)) * (s + z) * u_transposed
        s = -A @ v
        approximate_solution = approximate_solution + s
        increment_norm = np.linalg.norm(s)
        if increment_norm < tolerance:
            print(f"A função convergiu com sucesso em {i + 1} iterações.")
            return approximate_solution
    raise RuntimeError("Função não convergiu.")


def simulate_time_for_newton():
    logger = Logger()
    plotter = Plotter(logger)
    log_target = NewtonLoggerKeys.time
    x_0 = [10., 10., 10., 10., 10.]
    time_stress(newton, logger, 30, x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)

    print(f"Os valores logados foram os seguintes: "
          f"{logger.return_specific_key_values(log_target)}")
    print(f"O desvio padrão dos valores é: {np.std(logger.return_specific_key_values(log_target))}")
    plotter.plot_y_key(log_target)


def simulate_time_for_broyden():
    logger = Logger()
    plotter = Plotter(logger)
    log_target = BroydenLoggerKeys.time
    x_0 = [10., 10., 10., 10., 10.]
    time_stress(newton, logger, 30, x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)

    print(f"Os valores logados foram os seguintes: "
          f"{logger.return_specific_key_values(log_target)}")
    if log_target == BroydenLoggerKeys.time:
        print(f"O desvio padrão dos valores é: {np.std(logger.return_specific_key_values(log_target))}")
    plotter.plot_y_key(log_target)


def _main():
    x_0 = [10., 10., 10., 10., 10.]
    x_0 = [1., 30., 1., 1., 1.]
    logger = Logger()
    # log_target = NewtonLoggerKeys.residual_norm
    # plotter = Plotter(logger)
    #
    result = newton(x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)
    print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {result}.")
    #
    # print(f"Os valores logados foram os seguintes: "
    #       f"{logger.return_specific_key_values(log_target)}")
    # # print(f"O desvio padrão dos valores é: {np.std(logger.return_specific_key_values(log_target))}")
    #
    # plotter.plot_y_key(log_target)

    # x_0 = np.matrix([10., 10., 10., 10., 10.]).T
    x_0 = np.matrix([1., 30., 1., 1., 1.]).T
    result = broyden(x_0, exercise_function, jacobian_of_exercise_function, 1e-10)
    print(f"A solução para esse sistema de equações, utilizando o método de Broyden, é: {result}.")


if __name__ == '__main__':
    _main()
