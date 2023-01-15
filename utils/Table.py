from tabulate import tabulate

from constants import NewtonLoggerKeys, BroydenLoggerKeys, CommonKeys
from utils.Logger import Logger


def build_five_keys_entry(index: int, values: list):
    return index, values[0], values[1], values[2], values[3], values[4]


def build_one_key_entry(index: int, value):
    return index, value


def build_iterations_entry(index: int, values: dict):
    return index, values['step'], values['iterations']


def get_table_builder(target: NewtonLoggerKeys | BroydenLoggerKeys):
    if target in [NewtonLoggerKeys.x, BroydenLoggerKeys.x, NewtonLoggerKeys.residual, BroydenLoggerKeys.residual]:
        return ['iteration', 'x_1', 'x_2', 'x_3', 'x_4', 'x_5'], build_five_keys_entry
    elif target is CommonKeys.time:
        return ['iteration', 'time (s)'], build_one_key_entry
    elif target in [NewtonLoggerKeys.number_of_iterations, BroydenLoggerKeys.number_of_iterations]:
        return ['iteration', 'step size', 'number of iterations'], build_iterations_entry
    else:
        raise NotImplementedError("Target value doesn't have a table format yet.")


def build_table(target: NewtonLoggerKeys | BroydenLoggerKeys, logger: Logger):
    headers, entry_builder = get_table_builder(target)
    logs = logger.return_specific_key_values(target)

    indexes = [i for i in range(len(logs))]
    results = logger.return_specific_key_values(target)
    table = [entry_builder(index, values) for (index, values) in zip(indexes, results)]

    print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
