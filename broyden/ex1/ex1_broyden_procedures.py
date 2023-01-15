import itertools

import numpy as np

from broyden.broyden_method import broyden
from broyden.broyden_utils import DomainProvider, BroydenLimitReportEntry
from constants import BroydenLoggerKeys, exercise_function, jacobian_of_exercise_function, OPTIMAL_BROYDEN_MAXIMUM, OPTIMAL_BROYDEN_MINIMUM
from utils.Logger import Logger
from utils.Plotter import Plotter
from utils.Table import build_table
from utils.utils import time_stress


def simulate_time_for_broyden():
    logger = Logger()
    plotter = Plotter(logger)
    log_target = BroydenLoggerKeys.time
    x_0 = [10., 10., 10., 10., 10.]
    provider = DomainProvider(maximum=OPTIMAL_BROYDEN_MAXIMUM, minimum=OPTIMAL_BROYDEN_MINIMUM)
    time_stress(broyden, logger, 30, np.matrix(x_0).T, exercise_function, jacobian_of_exercise_function, 1e-10, logger, provider)

    values = logger.return_specific_key_values(log_target)
    print(f"O desvio padrão dos valores é: {np.std(values)}")
    print(f"O tempo máximo foi de {np.max(values)} s")
    print(f"O tempo mínimo foi de {np.min(values)} s")
    print(f"A média dos valores é: {np.mean(values)}")
    plotter.plot_y_key(log_target, unit="time (s)", graph_title="Broyden time in seconds")
    build_table(BroydenLoggerKeys.time, logger)


def estimate_solution():
    logger = Logger()
    x_0 = [10., 10., 10., 10., 10.]
    provider = DomainProvider(maximum=OPTIMAL_BROYDEN_MAXIMUM, minimum=OPTIMAL_BROYDEN_MINIMUM)
    estimated_solution = broyden(np.matrix(x_0).T, exercise_function, jacobian_of_exercise_function, 1e-10, logger, provider)

    print(f"A solução para esse sistema de equações, utilizando o método de Broyden, é: {estimated_solution}.")

    build_table(BroydenLoggerKeys.x, logger)


def estimate_residual():
    def plot_modifier(pyplot):
        pyplot.xticks(rotation=90)

    logger = Logger()
    plotter = Plotter(logger)
    log_target = BroydenLoggerKeys.residual_norm
    x_0 = [10., 10., 10., 10., 10.]
    provider = DomainProvider(maximum=OPTIMAL_BROYDEN_MAXIMUM, minimum=OPTIMAL_BROYDEN_MINIMUM)
    broyden(np.matrix(x_0).T, exercise_function, jacobian_of_exercise_function, 1e-10, logger, provider)

    plotter.plot_y_key(log_target, unit='', pyplot_modifiers=plot_modifier)
    build_table(BroydenLoggerKeys.residual, logger)


def simulate_domain_limits_for_broyden():
    maximum_values = [i for i in range(30, 100)]
    minimum_values = [i for i in np.arange(1e-5, 3e-3, 1e-4)]

    combinations = itertools.product(maximum_values, minimum_values)
    results = []
    for index, combination in enumerate(combinations):
        maximum, minimum = combination
        provider = DomainProvider(maximum=maximum, minimum=minimum)

        try:
            logger = Logger()
            x_0 = [10., 10., 10., 10., 10.]
            _, iterations = broyden(np.matrix(x_0).T, exercise_function, jacobian_of_exercise_function, 1e-10, logger, provider)

            report_entry = BroydenLimitReportEntry(provider, iterations)
            results.append(report_entry)
        except (RuntimeError, ZeroDivisionError):
            pass

    results.sort(reverse=True)
    print(results)
