from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Union

from dlplan.core import Boolean, Numerical


class Feature(ABC):

    @abstractmethod
    def is_boolean(self):
        pass

    @abstractmethod
    def is_numerical(self):
        pass


@dataclass
class DLPlanFeature(Feature):
    """ A single feature with custom complexity. """
    _dlplan_feature: Union[Boolean, Numerical]
    _complexity: int

    def is_boolean(self):
        return isinstance(self.dlplan_feature, Boolean)
    
    def is_numerical(self):
        return isinstance(self.dlplan_feature, Numerical)

    @property
    def dlplan_feature(self):
        return self._dlplan_feature

    @property
    def complexity(self):
        return self._complexity

    def __eq__(self, other: "DLPlanFeature"):
        return self.dlplan_feature == other.dlplan_feature

    def __hash__(self):
        return hash(str(self.dlplan_feature))


@dataclass
class FeaturePool:
    """ Stores the generated pool of features. """
    features: List[Feature]

