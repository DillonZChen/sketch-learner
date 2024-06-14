from typing import Dict, List, Union

FeatureValuations = List[Union[bool, int]]

PerStateFeatureValuations = Dict[int, FeatureValuations]
