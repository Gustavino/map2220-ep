class Logger:
    def __init__(self):
        self.entries = []

    def log_value(self, variable_name: str, value):
        entry = {variable_name: value}
        self.entries.append(entry)

    def return_specific_key_values(self, key: str):
        filtered = filter(lambda entry: list(entry.keys())[0] == key, self.entries)
        return list(map(lambda entry: list(entry.values())[0], filtered))
