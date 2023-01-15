import numpy as np

from constants import NewtonLoggerKeys, exercise_function, jacobian_of_exercise_function
from newton.newton_method import newton
from utils.Logger import Logger
from utils.Plotter import Plotter
from utils.Table import build_table
from utils.utils import time_stress


def simulate_time_for_newton():
    logger = Logger()
    plotter = Plotter(logger)
    log_target = NewtonLoggerKeys.time
    x_0 = [10., 10., 10., 10., 10.]
    time_stress(newton, logger, 30, x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)

    values = logger.return_specific_key_values(log_target)
    print(f"O desvio padrão dos valores é: {np.std(values)}")
    print(f"A média dos valores é: {np.mean(values)}")
    print(f"O tempo máximo foi de {np.max(values)} s")
    print(f"O tempo mínimo foi de {np.min(values)} s")
    plotter.plot_y_key(log_target, 'time (s)', graph_title='estimated time - newton - 30 iterations')
    build_table(NewtonLoggerKeys.time, logger)


def estimate_solution():
    logger = Logger()
    x_0 = [10., 10., 10., 10., 10.]
    estimated_solution = newton(x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)

    print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {estimated_solution}.")

    build_table(NewtonLoggerKeys.x, logger)


def estimate_residual():
    logger = Logger()
    plotter = Plotter(logger)
    log_target = NewtonLoggerKeys.residual_norm
    x_0 = [10., 10., 10., 10., 10.]
    newton(x_0, exercise_function, jacobian_of_exercise_function, 1e-10, logger)

    plotter.plot_y_key(log_target, '')
    build_table(NewtonLoggerKeys.residual, logger)


if __name__ == '__main__':
    simulate_time_for_newton()
