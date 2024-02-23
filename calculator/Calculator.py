class Calculator:

    def __init__(self) -> None:
        # initialise result value
        self.result = 0
    def add(self, *values: float):
        if len(values) != 0:
            for value in values:
                self.result += value
        return self.result

    def sub(self, *values: float):
        if len(values) != 0:
            for value in values:
                self.result -= value
        return self.result

    def mul(self, *values: float):
        if len(values) != 0:
            for value in values:
                self.result *= value
        return self.result

    def div(self, *values: float):
        if len(values) != 0:
            for value in values:
                self.result /= value
        return self.result
