from matplotlib import pyplot

from utils.Logger import Logger


class Plotter:
    def __init__(self, logger: Logger):
        self._logger = logger

    def plot_keys(self, x_key, y_key):
        fig, ax = pyplot.subplots()
        x = self._logger.return_specific_key_values(x_key)
        y = self._logger.return_specific_key_values(y_key)
        ax.bar(x, y)
        pyplot.show()

    def plot_y_key(self, y_key):
        fig, ax = pyplot.subplots()

        y = self._logger.return_specific_key_values(y_key)
        x = [i for i in range(len(y))]

        # ax.scatter(x, y, color='red', s=50, marker='^')
        ax.plot(x, y, color='red', linewidth=2, linestyle='-')

        # ax.set_ylim([1e-14, 1e-3])
        # ax.set_xlim([4, 10])

        ax.set_xticks(x)
        ax.set_xticklabels(x)

        pyplot.show()
