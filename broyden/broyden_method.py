import numpy as np

from broyden.broyden_utils import DomainProvider
from constants import MAXIMUM_ITERATIONS, BroydenLoggerKeys
from utils.Logger import Logger


def broyden(x_0: np.matrix, function: callable, jacobian: callable, tolerance: float, logger: Logger,
            provider: DomainProvider):
    def log_residual(new_v):
        logger.log_value(BroydenLoggerKeys.residual, new_v)
        logger.log_value(BroydenLoggerKeys.residual_norm, np.linalg.norm(new_v, -np.inf))

    def keep_in_domain(current_solution: np.matrix):
        maximum = provider.max
        minimum = provider.min
        for index in range(current_solution.size):
            if current_solution[index][0] < minimum:
                current_solution[index][0] = minimum
            elif current_solution[index][0] > maximum:
                current_solution[index][0] = maximum

    a_0 = np.matrix(jacobian(x_0))
    v: np.matrix = np.matrix(function(x_0)).T
    A = np.linalg.inv(a_0)
    s = -A @ v
    approximate_solution = x_0 + s
    logger.log_value(BroydenLoggerKeys.x, approximate_solution)
    for i in range(int(MAXIMUM_ITERATIONS) - 1):
        keep_in_domain(current_solution=approximate_solution)
        w = v
        v = np.matrix(function(approximate_solution)).T
        log_residual(v)

        y = v - w
        z = -A @ y
        p = -s.T @ z
        u_transposed = s.T @ A
        A = A + (1 / p.item(0, 0)) * (s + z) * u_transposed
        s = -A @ v
        approximate_solution = approximate_solution + s

        logger.log_value(BroydenLoggerKeys.x, approximate_solution)
        logger.log_value(BroydenLoggerKeys.norm_of_x, np.linalg.norm(approximate_solution, -np.inf))

        increment_norm = np.linalg.norm(s)

        logger.log_value(BroydenLoggerKeys.increment, s)
        logger.log_value(BroydenLoggerKeys.increment_norm, np.linalg.norm(s, -np.inf))
        if increment_norm < tolerance:
            print(f"A função convergiu com sucesso em {i + 1} iterações.")
            return approximate_solution, i + 1
    raise RuntimeError("Função não convergiu.")
