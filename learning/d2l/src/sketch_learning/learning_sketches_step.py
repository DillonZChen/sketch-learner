import logging

from .asp.sketch_asp_factory import SketchASPFactory
from .domain_data.domain_data_factory import DomainDataFactory
from .instance_data.instance_data_factory import InstanceDataFactory
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
    domain_data = DomainDataFactory().make_domain_data(config)
    instance_datas = InstanceDataFactory().make_instance_datas(config, domain_data)
    tuple_graph_datas = TupleGraphDataFactory(config.width).make_tuple_graph_datas(instance_datas)

    i = 0
    selected_instance_idxs = [0]
    largest_unsolved_instance_idx = 0
    timer = CountDownTimer(config.timeout)
    while not timer.is_expired():
        print("================================================================================")
        logging.info(f"Iteration instance selection: {i}")
        print("================================================================================")
        selected_instance_datas = [instance_datas[instance_idx] for instance_idx in selected_instance_idxs]
        print(f"Number of selected instances: {len(selected_instance_datas)}")
        for selected_instance_data in selected_instance_datas:
            print(str(selected_instance_data.instance_information.instance_filename), selected_instance_data.transition_system.get_num_states())
        selected_tuple_graph_datas = [tuple_graph_datas[instance_idx] for instance_idx in selected_instance_idxs]
        state_pair_datas = [StatePairDataFactory().make_state_pairs_from_tuple_graph_data(tuple_graph_data) for tuple_graph_data in selected_tuple_graph_datas]
        dlplan_states = []
        for selected_instance_data in selected_instance_datas:
            dlplan_states.extend([(selected_instance_data.transition_system.states_by_index[0], selected_instance_data.transition_system.states_by_index[s_idx]) for s_idx in range(selected_instance_data.transition_system.get_num_states())])
        domain_feature_data = DomainFeatureDataFactory().make_domain_feature_data(config, domain_data, dlplan_states)
        instance_feature_datas = [InstanceFeatureDataFactory().make_instance_feature_data(instance_data, domain_feature_data) for instance_data in selected_instance_datas]
        rule_equivalence_data, state_pair_equivalence_datas = StatePairEquivalenceDataFactory().make_equivalence_datas(state_pair_datas, domain_feature_data, instance_feature_datas)
        tuple_graph_equivalence_datas = [TupleGraphEquivalenceDataFactory().make_equivalence_data(instance_data, tuple_graph_data, state_pair_equivalence_data) for instance_data, tuple_graph_data, state_pair_equivalence_data in zip(selected_instance_datas, selected_tuple_graph_datas, state_pair_equivalence_datas)]

        # 1.3. Create and solve ASP
        sketch_asp_factory = SketchASPFactory(config)
        facts = sketch_asp_factory.make_facts(selected_instance_datas, selected_tuple_graph_datas, domain_feature_data, rule_equivalence_data, state_pair_equivalence_datas, tuple_graph_equivalence_datas)
        sketch_asp_factory.ground(facts)
        symbols = sketch_asp_factory.solve()
        sketch_asp_factory.print_statistics()
        sketch = Sketch(DlplanPolicyFactory().make_dlplan_policy_from_answer_set(symbols, domain_feature_data), config.width)
        logging.info("Learned the following sketch:")
        print(sketch.dlplan_policy.str())

        # Step 2: try the sketch on all instances until there are
        # (1) either no more instances then we return the sketch, or
        # (2) the sketch fails then we add the instance and do another iteration.
        all_solved = True
        assert all([sketch.solves(instance_data, tuple_graph_data) for instance_data, tuple_graph_data in zip(selected_instance_datas, selected_tuple_graph_datas)])
        for instance_idx, (instance_data, tuple_graph_data) in enumerate(zip(instance_datas, tuple_graph_datas)):
            if not sketch.solves(instance_data, tuple_graph_data):
                all_solved = False
                if instance_idx > largest_unsolved_instance_idx:
                    largest_unsolved_instance_idx = instance_idx
                    selected_instance_idxs = [instance_idx]
                else:
                    selected_instance_idxs.append(instance_idx)
                break
        if all_solved:
            break
        i += 1

    print("================================================================================")
    print("Summary: ")
    print("================================================================================")
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

