from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

from dlplan.core import Boolean, DenotationsCaches, Numerical
from dlplan.core import State as DLPlanState


class Feature(ABC):
    """Abstract Base Class for features."""

    _complexity: int

    @abstractmethod
    def is_boolean(self):
        pass

    @abstractmethod
    def is_numerical(self):
        pass

    @abstractmethod
    def evaluate(self, state: DLPlanState, cache=None):
        """
        Evaluates the given state using the feature pool.

        Args:
            state (DLPlanState): The state to be evaluated.
            cache (optional): A cache object to store intermediate results. Usually features
            are not evaluated independently so it is faster to batch evaluate them all at once
            and cache them such as in DLPlan or WLPlan.

        Returns:
            None
        """
        pass

    @property
    def complexity(self):
        return self._complexity


@dataclass
class WLPlanFeature(Feature):
    @property
    def dlplan_feature(self):
        raise RuntimeError(
            "WLPlanFeature does not have a DLPlan feature. This is a placeholder and this error likely called because you wanted to construct DLPlan policy rules which is not implemented yet."
        )


@dataclass
class DLPlanFeature(Feature):
    """A single feature with custom complexity."""

    _dlplan_feature: Union[Boolean, Numerical]
    _complexity: int

    def is_boolean(self):
        return isinstance(self.dlplan_feature, Boolean)

    def is_numerical(self):
        return isinstance(self.dlplan_feature, Numerical)

    def evaluate(self, state: DLPlanState, cache: DenotationsCaches):
        assert cache is not None
        assert isinstance(cache, DenotationsCaches)
        assert isinstance(state, DLPlanState)
        return self.dlplan_feature.evaluate(state, cache)

    @property
    def dlplan_feature(self):
        return self._dlplan_feature

    def __eq__(self, other: "DLPlanFeature"):
        return self.dlplan_feature == other.dlplan_feature

    def __hash__(self):
        return hash(str(self.dlplan_feature))
