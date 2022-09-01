#ifndef DLPLAN_INCLUDE_DLPLAN_POLICY_H_
#define DLPLAN_INCLUDE_DLPLAN_POLICY_H_

#include <unordered_set>
#include <vector>
#include <memory>
#include <iostream>
#include <string>

#include "evaluator.h"
#include "core.h"


namespace dlplan::policy {
class RuleImpl;
class PolicyImpl;
class PolicyBuilderImpl;
class PolicyReaderImpl;
class PolicyWriterImpl;
class EvaluationContext;


/**
 * All different kinds of conditions.
 */
class BaseCondition : public utils::Cachable {
private:
    std::shared_ptr<const core::BaseElement> m_base_feature;
    int m_index;

protected:
    BaseCondition(std::shared_ptr<const core::BaseElement> base_feature, int index=-1);

public:
    // Condition is not copieable because it must live in the cache.
    // For construction we need it to be moveable.
    // However, moving cannot be abused because Condition is always const
    BaseCondition(const BaseCondition& other) = delete;
    BaseCondition& operator=(const BaseCondition& other) = delete;
    BaseCondition(BaseCondition&& other);
    BaseCondition& operator=(BaseCondition&& other);
    virtual ~BaseCondition();

    virtual bool evaluate(evaluator::EvaluationContext& source_context) const = 0;

    virtual std::string compute_repr() const = 0;

    std::string str() const;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    int get_index() const;
    std::shared_ptr<const core::BaseElement> get_base_feature() const;
};


/**
 * All different kinds of effects.
 */
class BaseEffect : public utils::Cachable {
private:
    std::shared_ptr<const core::BaseElement> m_base_feature;
    int m_index;

protected:
    BaseEffect(std::shared_ptr<const core::BaseElement> base_feature, int index=-1);

public:
    // Effect is not copieable because it must live in the cache.
    // For construction we need it to be moveable.
    // However, moving cannot be abused because Effect is always const
    BaseEffect(const BaseEffect& other) = delete;
    BaseEffect& operator=(const BaseEffect& other) = delete;
    BaseEffect(BaseEffect&& other);
    BaseEffect& operator=(BaseEffect&& other);
    virtual ~BaseEffect();

    virtual bool evaluate(evaluator::EvaluationContext& source_context, evaluator::EvaluationContext& target_context) const = 0;

    virtual std::string compute_repr() const = 0;

    std::string str() const;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    int get_index() const;
    std::shared_ptr<const core::BaseElement> get_base_feature() const;
};


/**
 * A rule over Boolean and numerical features has form C -> E
 * where C is set of feature conditions and E is set of feature effects
 */
class Rule : public utils::Cachable {
private:
    std::vector<std::shared_ptr<const BaseCondition>> m_conditions;
    std::vector<std::shared_ptr<const BaseEffect>> m_effects;
    int m_index;

private:
    Rule(std::vector<std::shared_ptr<const BaseCondition>>&& conditions,
        std::vector<std::shared_ptr<const BaseEffect>>&& effects,
        int index=-1);
    friend class PolicyBuilderImpl;

public:
    // Rule is not copieable because it must live in the cache.
    // For construction we need it to be moveable.
    // However, moving cannot be abused because Rule is always const
    Rule(const Rule& other) = delete;
    Rule& operator=(const Rule& other) = delete;
    Rule(Rule&& other);
    Rule& operator=(Rule&& other);
    ~Rule();

    bool evaluate_conditions(evaluator::EvaluationContext& source_context) const;
    bool evaluate_effects(evaluator::EvaluationContext& source_context, evaluator::EvaluationContext& target_context) const;

    std::string compute_repr() const;

    std::string str() const;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    int get_index() const;
    std::vector<std::shared_ptr<const BaseCondition>> get_conditions() const;
    std::vector<std::shared_ptr<const BaseEffect>> get_effects() const;
};


/**
 * A policy is a set of rules over Boolean and numerical features.
 */
class Policy {
private:
    std::vector<std::shared_ptr<const core::Boolean>> m_boolean_features;
    std::vector<std::shared_ptr<const core::Numerical>> m_numerical_features;
    std::vector<std::shared_ptr<const Rule>> m_rules;

private:
    Policy(const std::vector<std::shared_ptr<const core::Boolean>>& boolean_features,
           const std::vector<std::shared_ptr<const core::Numerical>>& numerical_features,
           const std::vector<std::shared_ptr<const Rule>>& rules);
    friend class PolicyBuilderImpl;

public:
    Policy(const Policy& other);
    Policy& operator=(const Policy& other);
    Policy(Policy&& other);
    Policy& operator=(Policy&& other);
    ~Policy();

    /**
     * Approach 1: naive approach to evaluate (s,s')
     */
    std::shared_ptr<const Rule> evaluate_lazy(evaluator::EvaluationContext& source_context, evaluator::EvaluationContext& target_context);

    /**
     * Approach 2: optimized approach for evaluating pairs with similar source state s, i.e., (s,s1), (s,s2), ..., (s,sn)
     */
    std::vector<std::shared_ptr<const Rule>> evaluate_conditions_eager(evaluator::EvaluationContext& source_context);
    std::shared_ptr<const Rule> evaluate_effects_lazy(evaluator::EvaluationContext& source_context, evaluator::EvaluationContext& target_context, const std::vector<std::shared_ptr<const Rule>>& rules);

    std::string compute_repr() const;

    std::string str() const;

    std::vector<std::shared_ptr<const Rule>> get_rules() const;
    std::vector<std::shared_ptr<const core::Boolean>> get_boolean_features() const;
    std::vector<std::shared_ptr<const core::Numerical>> get_numerical_features() const;
};


class PolicyBuilder {
private:
    utils::pimpl<PolicyBuilderImpl> m_pImpl;

public:
    PolicyBuilder();
    PolicyBuilder(const PolicyBuilder& other);
    PolicyBuilder& operator=(const PolicyBuilder& other);
    PolicyBuilder(PolicyBuilder&& other);
    PolicyBuilder& operator=(PolicyBuilder&& other);
    ~PolicyBuilder();

    /**
     * Uniquely adds features.
     */
    std::shared_ptr<const core::Boolean> add_boolean_feature(core::Boolean b);
    std::shared_ptr<const core::Numerical> add_numerical_feature(core::Numerical n);

    /**
     * Uniquely adds a condition (resp. effect) to the policy and returns it.
     */
    std::shared_ptr<const BaseCondition> add_pos_condition(std::shared_ptr<const core::Boolean> b);
    std::shared_ptr<const BaseCondition> add_neg_condition(std::shared_ptr<const core::Boolean> b);
    std::shared_ptr<const BaseCondition> add_gt_condition(std::shared_ptr<const core::Numerical> n);
    std::shared_ptr<const BaseCondition> add_eq_condition(std::shared_ptr<const core::Numerical> n);
    std::shared_ptr<const BaseEffect> add_pos_effect(std::shared_ptr<const core::Boolean> b);
    std::shared_ptr<const BaseEffect> add_neg_effect(std::shared_ptr<const core::Boolean> b);
    std::shared_ptr<const BaseEffect> add_bot_effect(std::shared_ptr<const core::Boolean> b);
    std::shared_ptr<const BaseEffect> add_inc_effect(std::shared_ptr<const core::Numerical> n);
    std::shared_ptr<const BaseEffect> add_dec_effect(std::shared_ptr<const core::Numerical> n);
    std::shared_ptr<const BaseEffect> add_bot_effect(std::shared_ptr<const core::Numerical> n);

    /**
     * Uniquely adds a rule to the policy and returns it.
     */
    std::shared_ptr<const Rule> add_rule(
        std::vector<std::shared_ptr<const BaseCondition>>&& conditions,
        std::vector<std::shared_ptr<const BaseEffect>>&& effects);

    /**
     * TODO: - sort features by their runtime complexity.
     *       - sort rules by sum of runtime complexities of underlying features.
     *       - compute invariants
     */
    Policy get_result();
};


/**
 * PolicyMinimizer provides methods to minimize the number of rules in a policy
 * such that it distinguishes the same true and false state pairs.
 */
class PolicyMinimizer {
private:
public:
    PolicyMinimizer();
    PolicyMinimizer(const PolicyMinimizer& other);
    PolicyMinimizer& operator=(const PolicyMinimizer& other);
    PolicyMinimizer(PolicyMinimizer&& other);
    PolicyMinimizer& operator=(PolicyMinimizer&& other);
    ~PolicyMinimizer();

    Policy minimize_greedy(const Policy& policy, const core::StatePairs& true_state_pairs, const core::StatePairs& false_state_pairs) const;
};


/**
 * PolicyReader for reading general policy from bytestream.
 */
class PolicyReader {
private:
    utils::pimpl<PolicyReaderImpl> m_pImpl;

public:
    PolicyReader();
    PolicyReader(const PolicyReader& other);
    PolicyReader& operator=(const PolicyReader& other);
    PolicyReader(PolicyReader&& other);
    PolicyReader& operator=(PolicyReader&& other);
    ~PolicyReader();

    Policy read(const std::string& data, core::SyntacticElementFactory& factory) const;
};

/**
 * PolicyWriter for writing general policy to bytestream.
 */
class PolicyWriter {
    utils::pimpl<PolicyWriterImpl> m_pImpl;

public:
    PolicyWriter();
    PolicyWriter(const PolicyWriter& other);
    PolicyWriter& operator=(const PolicyWriter& other);
    PolicyWriter(PolicyWriter&& other);
    PolicyWriter& operator=(PolicyWriter&& other);
    ~PolicyWriter();

    std::string write(const Policy& policy) const;
};

}

#endif