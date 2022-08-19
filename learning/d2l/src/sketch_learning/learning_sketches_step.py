import logging

from termcolor import colored
from typing import List

from .asp.sketch_asp_factory import SketchASPFactory
from .domain_data.domain_data_factory import DomainDataFactory
from .instance_data.instance_data import InstanceData
from .instance_data.instance_data_factory import InstanceDataFactory
from .instance_data.tuple_graph_data import TupleGraphData
from .instance_data.tuple_graph_data_factory import TupleGraphDataFactory
from .iteration_data.domain_feature_data_factory import DomainFeatureDataFactory
from .iteration_data.instance_feature_data_factory import InstanceFeatureDataFactory
from .iteration_data.dlplan_policy_factory import DlplanPolicyFactory
from .iteration_data.sketch import Sketch
from .iteration_data.state_pair_equivalence_data_factory import StatePairEquivalenceDataFactory
from .iteration_data.tuple_graph_equivalence_data_factory import  TupleGraphEquivalenceDataFactory
from .iteration_data.state_pair_data_factory import StatePairDataFactory
from .returncodes import ExitCode
from .util.timer import CountDownTimer


def run(config, data, rng):
    logging.info(colored(f"Initializing DomainData...", "green", "on_grey"))
    domain_data = DomainDataFactory().make_domain_data(config)
    logging.info(colored(f"..done", "green", "on_grey"))

    logging.info(colored(f"Initializing InstanceDatas...", "green", "on_grey"))
    instance_datas = InstanceDataFactory().make_instance_datas(config, domain_data)
    logging.info(colored(f"..done", "green", "on_grey"))

    logging.info(colored(f"Initializing TupleGraphDatas...", "green", "on_grey"))
    tuple_graph_datas = TupleGraphDataFactory(config.width).make_tuple_graph_datas(instance_datas)
    logging.info(colored(f"..done", "green", "on_grey"))

    i = 0
    selected_instance_idxs = [0]
    timer = CountDownTimer(config.timeout)
    while not timer.is_expired():
        logging.info(colored(f"Iteration: {i}", "red", "on_grey"))
        selected_instance_datas = [instance_datas[instance_idx] for instance_idx in selected_instance_idxs]
        print(f"Number of selected instances: {len(selected_instance_datas)}")
        for selected_instance_data in selected_instance_datas:
            print(str(selected_instance_data.instance_information.instance_filename), selected_instance_data.transition_system.get_num_states())
        selected_tuple_graph_datas = [tuple_graph_datas[instance_idx] for instance_idx in selected_instance_idxs]

        logging.info(colored(f"Initializing StatePairDatas...", "blue", "on_grey"))
        state_pair_datas = [StatePairDataFactory().make_state_pairs_from_tuple_graph_data(tuple_graph_data) for tuple_graph_data in selected_tuple_graph_datas]
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Initializing DomainFeatureData...", "blue", "on_grey"))
        dlplan_state_pairs = []
        for selected_instance_data in selected_instance_datas:
            dlplan_state_pairs.extend([(selected_instance_data.transition_system.states_by_index[0], selected_instance_data.transition_system.states_by_index[s_idx]) for s_idx in range(selected_instance_data.transition_system.get_num_states())])
        print("Number of dlplan state pairs:", len(dlplan_state_pairs))
        domain_feature_data = DomainFeatureDataFactory().make_domain_feature_data(config, domain_data, dlplan_state_pairs)
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Initializing InstanceFeatureDatas...", "blue", "on_grey"))
        instance_feature_datas = [InstanceFeatureDataFactory().make_instance_feature_data(instance_data, domain_feature_data) for instance_data in selected_instance_datas]
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Initializing StatePairEquivalenceDatas...", "blue", "on_grey"))
        rule_equivalence_data, state_pair_equivalence_datas = StatePairEquivalenceDataFactory().make_equivalence_datas(state_pair_datas, domain_feature_data, instance_feature_datas)
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Initializing TupleGraphEquivalenceDatas...", "blue", "on_grey"))
        tuple_graph_equivalence_datas = [TupleGraphEquivalenceDataFactory().make_equivalence_data(instance_data, tuple_graph_data, state_pair_equivalence_data) for instance_data, tuple_graph_data, state_pair_equivalence_data in zip(selected_instance_datas, selected_tuple_graph_datas, state_pair_equivalence_datas)]
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Initializing Logic Program...", "blue", "on_grey"))
        sketch_asp_factory = SketchASPFactory(config)
        facts = sketch_asp_factory.make_facts(selected_instance_datas, selected_tuple_graph_datas, domain_feature_data, rule_equivalence_data, state_pair_equivalence_datas, tuple_graph_equivalence_datas)
        sketch_asp_factory.ground(facts)
        logging.info(colored(f"..done", "blue", "on_grey"))

        logging.info(colored(f"Solving Logic Program...", "blue", "on_grey"))
        symbols = sketch_asp_factory.solve()
        logging.info(colored(f"..done", "blue", "on_grey"))

        sketch_asp_factory.print_statistics()
        sketch = Sketch(DlplanPolicyFactory().make_dlplan_policy_from_answer_set(symbols, domain_feature_data), config.width)
        logging.info("Learned the following sketch:")
        print(sketch.dlplan_policy.str())

        logging.info(colored(f"Verifying learned sketch...", "blue", "on_grey"))
        assert all([sketch.solves(instance_data, tuple_graph_data) for instance_data, tuple_graph_data in zip(selected_instance_datas, selected_tuple_graph_datas)])
        all_solved, selected_instance_idxs = verify_sketch(sketch, instance_datas, tuple_graph_datas, selected_instance_idxs)
        logging.info(colored(f"..done", "blue", "on_grey"))

        if all_solved:
            break
        i += 1

    logging.info(colored("Summary:", "green"))
    print("Number of training instances:", len(instance_datas))
    print("Number of training instances included in the ASP:", len(selected_instance_datas))
    print("Number of states included in the ASP:", sum([len(instance_data.transition_system.states_by_index) for instance_data in selected_instance_datas]))
    print("Number of features in the pool:", len(domain_feature_data.boolean_features) + len(domain_feature_data.numerical_features))
    print("Numer of sketch rules:", len(sketch.dlplan_policy.get_rules()))
    print("Number of selected features:", len(sketch.dlplan_policy.get_boolean_features()) + len(sketch.dlplan_policy.get_numerical_features()))
    print("Maximum complexity of selected feature:", max([0] + [boolean_feature.get_boolean().compute_complexity() for boolean_feature in sketch.dlplan_policy.get_boolean_features()] + [numerical_feature.get_numerical().compute_complexity() for numerical_feature in sketch.dlplan_policy.get_numerical_features()]))
    print("Resulting sketch:")
    print(sketch.dlplan_policy.str())
    return ExitCode.Success, None


def verify_sketch(sketch: Sketch, instance_datas: List[InstanceData], tuple_graph_datas: List[TupleGraphData], selected_instance_idxs: List[int]):
    all_solved = True
    for instance_idx, (instance_data, tuple_graph_data) in enumerate(zip(instance_datas, tuple_graph_datas)):
        if not sketch.solves(instance_data, tuple_graph_data):
            all_solved = False
            if instance_idx > max(selected_instance_idxs):
                selected_instance_idxs = [instance_idx]
            else:
                selected_instance_idxs.append(instance_idx)
            break
    return all_solved, selected_instance_idxs
