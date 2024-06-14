from typing import List

from ..domain_data.domain_data import DomainData
from ..instance_data.instance_data import InstanceData
from .feature_valuations import FeatureValuations, PerStateFeatureValuations


def compute_per_state_feature_valuations(instance_datas: List[InstanceData], domain_data: DomainData) -> None:
    """Evaluates the features on all states."""
    for instance_data in instance_datas:
        per_state_feature_valuations: PerStateFeatureValuations = {}
        for s_idx, dlplan_state in instance_data.state_space.get_states().items():
            state_feature_valuations = instance_data.domain_data.feature_pool.evaluate(dlplan_state, dlplan_cache=instance_data.denotations_caches)
            per_state_feature_valuations[s_idx] = state_feature_valuations
        instance_data.per_state_feature_valuations = per_state_feature_valuations
