from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from dlplan.core import DenotationsCaches
from dlplan.core import State as DLPlanState
from learner.src.iteration_data.feature import Feature
from learner.src.iteration_data.feature_valuations import FeatureValuations


@dataclass
class FeaturePool(ABC):
    """Stores the generated pool of features."""

    _features: List[Feature]

    @abstractmethod
    def evaluate(self, state: DLPlanState, **kwargs) -> FeatureValuations:
        pass

    def __len__(self):
        return len(self._features)

    def __getitem__(self, index):
        return self._features[index]


class DLPlanFeaturePool(FeaturePool):
    def evaluate(self, state: DLPlanState, dlplan_cache: DenotationsCaches) -> FeatureValuations:
        state_feature_valuations: FeatureValuations = []
        for feature in self._features:
            state_feature_valuations.append(feature.evaluate(state, dlplan_cache))
        return state_feature_valuations

class WLPlanFeaturePool(FeaturePool):
    def evaluate(self, state: DLPlanState) -> FeatureValuations:
        raise NotImplementedError
