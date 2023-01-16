import numpy as np
from numpy.linalg import LinAlgError

from constants import NewtonLoggerKeys, MAXIMUM_ITERATIONS
from utils.Logger import Logger


# Processo de encontrar a solução de um sistema não linear. Omitiram-se comentários devido ao nome das variáveis ter sido escolhido
# de forma autoexplicativa.
def newton(x: list, function: callable, jacobian: callable, tolerance: float, logger: Logger):
    def log_residual(new_f_of_x):
        if i > 0:
            logger.log_value(NewtonLoggerKeys.residual, new_f_of_x)
            logger.log_value(NewtonLoggerKeys.residual_norm, np.linalg.norm(new_f_of_x, -np.inf))

    for i in range(int(MAXIMUM_ITERATIONS)):
        f_of_x = function(x)
        log_residual(f_of_x)

        logger.log_value(NewtonLoggerKeys.x, x)
        logger.log_value(NewtonLoggerKeys.norm_of_x, np.linalg.norm(x, -np.inf))

        jacobian_of_x = jacobian(x)

        y_increment = -np.linalg.solve(jacobian_of_x, f_of_x)

        x = x + y_increment
        increment_norm = np.linalg.norm(y_increment)

        logger.log_value(NewtonLoggerKeys.increment, y_increment)
        logger.log_value(NewtonLoggerKeys.increment_norm, np.linalg.norm(y_increment, -np.inf))

        if increment_norm < tolerance:
            print(f"A função convergiu com sucesso em {i} iterações.")
            return x, i
    raise RuntimeError("Função não convergiu.")
