import dlplan


def main():
    vocabulary_info = dlplan.VocabularyInfo()
    vocabulary_info.add_predicate("unary", 1)
    factory = dlplan.SyntacticElementFactory(vocabulary_info)
    boolean = factory.parse_boolean("b_empty(c_primitive(unary,0))")
    numerical = factory.parse_numerical("n_count(c_primitive(unary,0))")

    builder = dlplan.PolicyBuilder()
    b = builder.add_boolean_feature(boolean)
    n = builder.add_numerical_feature(numerical)
    print(type(b))
    b_neg_condition_0 = builder.add_neg_condition(b)
    b_bot_effect_0 = builder.add_bot_effect(b)
    n_gt_condition_0 = builder.add_gt_condition(n)
    n_dec_effect_0 = builder.add_dec_effect(n)
    r = builder.add_rule(
        [b_neg_condition_0, n_gt_condition_0],
        [b_bot_effect_0, n_dec_effect_0]
    )
    policy = builder.get_result()

    instance_info = dlplan.InstanceInfo(vocabulary_info)
    a0 = instance_info.add_atom("unary", ["A"])
    a1 = instance_info.add_atom("unary", ["B"])

    s0 = dlplan.State(instance_info, [], 0)
    s1 = dlplan.State(instance_info, [a0], 1)
    s2 = dlplan.State(instance_info, [a0, a1], 2)

    evaluation_cache = dlplan.EvaluationCache(len(policy.get_boolean_features()), len(policy.get_numerical_features()))
    s0_context = dlplan.EvaluationContext(s0, evaluation_cache)
    s1_context = dlplan.EvaluationContext(s1, evaluation_cache)
    s2_context = dlplan.EvaluationContext(s2, evaluation_cache)

    assert policy.evaluate_lazy(s2_context, s1_context)
    assert not policy.evaluate_lazy(s2_context, s0_context)
    assert not policy.evaluate_lazy(s1_context, s2_context)
    assert not policy.evaluate_lazy(s0_context, s2_context)

    print("Write policy:")
    print(policy.compute_repr())
    print()
    with open("policy.txt", "w") as f:
        f.write(dlplan.PolicyWriter().write(policy))

    with open("policy.txt", "r") as f:
        policy_in = dlplan.PolicyReader().read("\n".join(f.readlines()), factory)
    print(policy_in.compute_repr())
    print()



if __name__ == "__main__":
    main()
