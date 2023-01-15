from functools import partial

import numpy as np
from numpy.linalg import LinAlgError

from constants import NewtonLoggerKeys, exercise_function, Order, jacobian_with_finite_differences
from newton.newton_method import newton
from utils.Logger import Logger
from utils.Plotter import Plotter
from utils.Table import build_table
from utils.utils import time_stress

OPTIMAL_NEWTON_FIRST_ORDER_STEP = 1e-6
OPTIMAL_NEWTON_SECOND_ORDER_STEP = 1e-6


def _get_step_and_title(order: Order) -> (float, str):
    return (OPTIMAL_NEWTON_FIRST_ORDER_STEP, "Newton - Forward differences") if order == Order.FIRST \
        else (OPTIMAL_NEWTON_SECOND_ORDER_STEP, "Newton - Centered differences")


def simulate_time_for_newton():
    for order in [Order.FIRST, Order.SECOND]:
        step, graph_title = _get_step_and_title(order)

        logger = Logger()
        plotter = Plotter(logger)
        log_target = NewtonLoggerKeys.time
        x_0 = [10., 10., 10., 10., 10.]

        print(f"Order: {order}.")
        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        time_stress(newton, logger, 30, x_0, exercise_function, jacobian, 1e-10, logger)

        values = logger.return_specific_key_values(log_target)
        print(f"O desvio padrão dos valores é: {np.std(values)}")
        print(f"A média dos valores é: {np.mean(values)}")
        print(f"O tempo máximo foi de {np.max(values)} s")
        print(f"O tempo mínimo foi de {np.min(values)} s")
        plotter.plot_y_key(log_target, unit='time (s)', graph_title=graph_title)
        build_table(NewtonLoggerKeys.time, logger)


def estimate_solution():
    for order in [Order.FIRST, Order.SECOND]:
        step, _ = _get_step_and_title(order)
        logger = Logger()
        x_0 = [10., 10., 10., 10., 10.]

        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        estimated_solution = newton(x_0, exercise_function, jacobian, 1e-10, logger)

        print(f"Order: {order}.")
        print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {estimated_solution}.")

        build_table(NewtonLoggerKeys.x, logger)


def estimate_residual():
    for order in [Order.FIRST, Order.SECOND]:
        step, graph_title = _get_step_and_title(order)

        logger = Logger()
        plotter = Plotter(logger)
        log_target = NewtonLoggerKeys.residual_norm
        x_0 = [10., 10., 10., 10., 10.]

        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        print(f"Order: {order}.")
        newton(x_0, exercise_function, jacobian, 1e-10, logger)

        plotter.plot_y_key(log_target, graph_title)
        build_table(NewtonLoggerKeys.residual, logger)


def simulate_jacobian_steps():
    x_0 = [10., 10., 10., 10., 10.]
    steps = [1e-16 * (10 ** i) for i in range(0, 18)]
    for order in [Order.FIRST, Order.SECOND]:
        print(f"Starting for order: {order}")
        logger = Logger()
        for step in steps:
            try:
                jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
                _, iterations = newton(x_0, exercise_function, jacobian, 1e-10, logger)
                logger.log_value(NewtonLoggerKeys.number_of_iterations, {"step": step, "iterations": iterations})
            except LinAlgError:
                logger.log_value(NewtonLoggerKeys.number_of_iterations, {"step": step, "iterations": "!ERROR: Singular matrix"})
            except RuntimeError:
                logger.log_value(NewtonLoggerKeys.number_of_iterations, {"step": step, "iterations": "!ERROR: Maximum iterations"})
        build_table(NewtonLoggerKeys.number_of_iterations, logger)


# todo: remove this  main
if __name__ == '__main__':
    simulate_time_for_newton()
