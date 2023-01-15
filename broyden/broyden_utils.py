class DomainProvider:
    def __init__(self, maximum: int, minimum: float):
        self.max: int = maximum,
        self.min: float = minimum

    def get_info(self, index):
        return f'index = {index} - max: {self.max}, min: {self.min}'


class BroydenLimitReportEntry:
    def __init__(self, provider: DomainProvider, iterations_to_finish: int):
        self.maximum = provider.max[0]
        self.minimum = provider.min
        self.iterations_to_finish = iterations_to_finish

    def __ge__(self, other):
        return self.iterations_to_finish <= other.iterations_to_finish

    def __le__(self, other):
        return self.iterations_to_finish >= other.iterations_to_finish

    def __gt__(self, other):
        return self.iterations_to_finish < other.iterations_to_finish

    def __lt__(self, other):
        return self.iterations_to_finish > other.iterations_to_finish

    def __repr__(self):
        return f'Max: {self.maximum}, Min: {self.minimum} - Iterations: {self.iterations_to_finish}'
