from .fact import Fact


class FeatureComplexity(Fact):
    """ Defines the feature valuation in a given state. """
    def __init__(self, f_idx, f_complexity):
        super().__init__("complexity")
        self.f_idx = f_idx
        self.f_complexity = f_complexity

    def __str__(self):
        return f"{self.name}({self.f_idx}, {self.f_complexity}).\n"
