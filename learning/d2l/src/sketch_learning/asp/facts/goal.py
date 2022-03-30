from .fact import Fact


class Goal(Fact):
    """ Defines that a state is a goal state. """
    def __init__(self, instance_idx, s_idx):
        super().__init__("goal")
        self.instance_idx = instance_idx
        self.s_idx = s_idx

    def __str__(self):
        return f"{self.name}({self.instance_idx}, {self.s_idx}).\n"
