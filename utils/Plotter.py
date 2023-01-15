from matplotlib import pyplot

from utils.Logger import Logger


class Plotter:
    def __init__(self, logger: Logger):
        self._logger = logger

    def plot_y_key(self, y_key, unit: str,
                   graph_title: str = None, pyplot_modifiers: callable = None, axis_modifiers: callable = None,
                   y_values_unwrapper=None, x_values_unwrapper=None):
        fig, ax = pyplot.subplots(figsize=(9, 3))

        y = self._logger.return_specific_key_values(y_key)
        if y_values_unwrapper:
            y = y_values_unwrapper(y)

        if x_values_unwrapper:
            x = x_values_unwrapper(self._logger.return_specific_key_values(y_key))
        else:
            x = [i for i in range(1, len(y) + 1)]

        ax.plot(x, y, color='red', linewidth=2, linestyle='-')

        ax.set_xticks([i for i in range(1, len(y) + 1)])
        ax.set_xticklabels(x)

        pyplot.ylabel(unit)

        graph_title = graph_title if graph_title is not None else y_key
        pyplot.title(graph_title)

        if pyplot_modifiers:
            pyplot_modifiers(pyplot)
        if axis_modifiers:
            axis_modifiers(ax)

        pyplot.show()
