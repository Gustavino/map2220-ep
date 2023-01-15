import itertools
from functools import partial

import numpy as np
from numpy.linalg import LinAlgError

from broyden.broyden_method import broyden
from broyden.broyden_utils import DomainProvider, BroydenLimitReportEntry
from constants import BroydenLoggerKeys, exercise_function, OPTIMAL_BROYDEN_MAXIMUM, OPTIMAL_BROYDEN_MINIMUM, \
    Order, jacobian_with_finite_differences, OPTIMAL_BROYDEN_FIRST_ORDER_MAXIMUM, OPTIMAL_BROYDEN_FIRST_ORDER_MINIMUM, \
    OPTIMAL_BROYDEN_SECOND_ORDER_MAXIMUM, OPTIMAL_BROYDEN_SECOND_ORDER_MINIMUM
from utils.Logger import Logger
from utils.Plotter import Plotter
from utils.Table import build_table
from utils.utils import time_stress

OPTIMAL_BROYDEN_FIRST_ORDER_STEP = 1e-6
OPTIMAL_BROYDEN_SECOND_ORDER_STEP = 1e-4


def _get_execution_data(order: Order) -> (float, str):
    if order == Order.FIRST:
        return (OPTIMAL_BROYDEN_FIRST_ORDER_STEP, "Broyden - Forward differences",
                DomainProvider(maximum=OPTIMAL_BROYDEN_FIRST_ORDER_MAXIMUM, minimum=OPTIMAL_BROYDEN_FIRST_ORDER_MINIMUM))
    else:
        return (OPTIMAL_BROYDEN_SECOND_ORDER_STEP, "Broyden - Centered differences",
                DomainProvider(maximum=OPTIMAL_BROYDEN_SECOND_ORDER_MAXIMUM, minimum=OPTIMAL_BROYDEN_SECOND_ORDER_MINIMUM))


def simulate_time_for_broyden():
    for order in [Order.FIRST, Order.SECOND]:
        step, graph_title, provider = _get_execution_data(order)

        logger = Logger()
        plotter = Plotter(logger)
        log_target = BroydenLoggerKeys.time
        x_0 = [10., 10., 10., 10., 10.]

        # todo: comentar no relatorio de onde vieram esses valores
        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        time_stress(broyden, logger, 30, np.matrix(x_0).T, exercise_function, jacobian, 1e-10, logger, provider)

        print(f"O desvio padrão dos valores é: {np.std(logger.return_specific_key_values(log_target))}")
        print(f"A média dos valores é: {np.mean(logger.return_specific_key_values(log_target))}")
        plotter.plot_y_key(log_target, "time (s)", graph_title)
        build_table(BroydenLoggerKeys.time, logger)


def estimate_solution():
    for order in [Order.FIRST, Order.SECOND]:
        step, _, provider = _get_execution_data(order)
        logger = Logger()
        x_0 = [10., 10., 10., 10., 10.]

        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        estimated_solution = broyden(np.matrix(x_0).T, exercise_function, jacobian, 1e-10, logger, provider)

        print(f"A solução para esse sistema de equações, utilizando o método de Newton, é: {estimated_solution}.")

        build_table(BroydenLoggerKeys.x, logger)


def estimate_residual():
    def plot_modifier(pyplot):
        pyplot.xticks(rotation=90, fontsize=5)

    for order in [Order.FIRST, Order.SECOND]:
        step, graph_title, provider = _get_execution_data(order)

        logger = Logger()
        plotter = Plotter(logger)
        log_target = BroydenLoggerKeys.residual_norm
        x_0 = [10., 10., 10., 10., 10.]

        jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
        broyden(np.matrix(x_0).T, exercise_function, jacobian, 1e-10, logger, provider)

        plotter.plot_y_key(log_target, graph_title, pyplot_modifiers=plot_modifier)
        build_table(BroydenLoggerKeys.residual, logger)


# todo: maybe create table.
def simulate_domain_limits_for_broyden():
    maximum_values = [i for i in range(30, 100)]
    minimum_values = [i for i in np.arange(1e-5, 3e-3, 1e-4)]

    combinations = itertools.product(maximum_values, minimum_values)
    results = []
    for order in [Order.FIRST, Order.SECOND]:
        step, _ = _get_execution_data(order)
        for index, combination in enumerate(combinations):
            maximum, minimum = combination
            provider = DomainProvider(maximum=maximum, minimum=minimum)

            try:
                logger = Logger()
                x_0 = [10., 10., 10., 10., 10.]
                jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
                _, iterations = broyden(np.matrix(x_0).T, exercise_function, jacobian, 1e-10, logger, provider)

                report_entry = BroydenLimitReportEntry(provider, iterations)
                results.append(report_entry)
            except (RuntimeError, ZeroDivisionError):
                pass

        results.sort(reverse=True)
        print(results)


def simulate_jacobian_steps():
    # todo: delete
    # def plot_modifier(pyplot):
    #     pyplot.xticks(rotation=60, fontsize=7)
    #
    # def y_values_unwrapper(values: list):
    #     filtered = filter(lambda value: type(value['iterations']) is not str, values)
    #     return list(map(lambda entry: entry['iterations'], filtered))
    #
    # def x_values_unwrapper(values: list):
    #     filtered = filter(lambda value: type(value['iterations']) is not str, values)
    #     return list(map(lambda entry: entry['step'], filtered))

    x_0 = [10., 10., 10., 10., 10.]
    provider = DomainProvider(maximum=OPTIMAL_BROYDEN_MAXIMUM, minimum=OPTIMAL_BROYDEN_MINIMUM)
    steps = [1e-16 * (10 ** i) for i in range(0, 18)]
    # todo: delete
    # graph_title_template = 'Broyden - {} - Number of iterations'
    for order in [Order.FIRST, Order.SECOND]:
        print(f"Starting for order: {order}")
        logger = Logger()
        # todo: delete
        # plotter = Plotter(logger)
        # graph_title = graph_title_template.format('Forward differences') if order == Order.FIRST else graph_title_template.format(
        #     'Centered differences')
        for step in steps:
            try:
                jacobian = partial(jacobian_with_finite_differences, exercise_function, order, step)
                _, iterations = broyden(np.matrix(x_0).T, exercise_function, jacobian, 1e-10, logger, provider)
                logger.log_value(BroydenLoggerKeys.number_of_iterations, {"step": step, "iterations": iterations})
            except LinAlgError:
                logger.log_value(BroydenLoggerKeys.number_of_iterations, {"step": step, "iterations": "!ERROR: Singular matrix"})
            except RuntimeError:
                logger.log_value(BroydenLoggerKeys.number_of_iterations, {"step": step, "iterations": "!ERROR: Maximum iterations"})
            except ZeroDivisionError:
                logger.log_value(BroydenLoggerKeys.number_of_iterations, {"step": step, "iterations": "!ERROR: DEGENERATED"})

        build_table(BroydenLoggerKeys.number_of_iterations, logger)

        # todo: delete
        # plotter.plot_y_key(BroydenLoggerKeys.number_of_iterations, unit='iterations', graph_title=graph_title,
        #                    pyplot_modifiers=plot_modifier,
        #                    y_values_unwrapper=y_values_unwrapper, x_values_unwrapper=x_values_unwrapper)


# todo: remove this main.
if __name__ == '__main__':
    simulate_jacobian_steps()
