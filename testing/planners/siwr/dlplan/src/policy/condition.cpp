#include "condition.h"


namespace dlplan::policy {

BooleanCondition::BooleanCondition(std::shared_ptr<const core::Boolean> boolean)
    : BaseCondition(boolean), m_boolean(boolean) { }


NumericalCondition::NumericalCondition(std::shared_ptr<const core::Numerical> numerical)
    : BaseCondition(numerical), m_numerical(numerical) { }


PositiveBooleanCondition::PositiveBooleanCondition(std::shared_ptr<const core::Boolean> boolean_feature)
    : BooleanCondition(boolean_feature) { }

bool PositiveBooleanCondition::evaluate(const core::State& source_state, evaluator::EvaluationCache& cache) const {
    return cache.retrieve_or_evaluate(*m_boolean, source_state);
}

std::string PositiveBooleanCondition::compute_repr() const {
    return "(:c_b_pos " + std::to_string(m_boolean->get_index()) + ")";
}

std::shared_ptr<const BaseCondition> PositiveBooleanCondition::visit(PolicyBuilder& policy_builder) const {
    return policy_builder.add_pos_condition(policy_builder.add_boolean_feature(*m_boolean));
}


NegativeBooleanCondition::NegativeBooleanCondition(std::shared_ptr<const core::Boolean> boolean_feature)
    : BooleanCondition(boolean_feature) { }

bool NegativeBooleanCondition::evaluate(const core::State& source_state, evaluator::EvaluationCache& cache) const {
    return !cache.retrieve_or_evaluate(*m_boolean, source_state);
}

std::string NegativeBooleanCondition::compute_repr() const {
    return "(:c_b_neg " + std::to_string(m_boolean->get_index()) + ")";
}

std::shared_ptr<const BaseCondition> NegativeBooleanCondition::visit(PolicyBuilder& policy_builder) const {
    return policy_builder.add_neg_condition(policy_builder.add_boolean_feature(*m_boolean));
}


EqualNumericalCondition::EqualNumericalCondition(std::shared_ptr<const core::Numerical> numerical_feature)
    : NumericalCondition(numerical_feature) { }

bool EqualNumericalCondition::evaluate(const core::State& source_state, evaluator::EvaluationCache& cache) const {
    return cache.retrieve_or_evaluate(*m_numerical, source_state) == 0;
}

std::string EqualNumericalCondition::compute_repr() const {
    return "(:c_n_eq " + std::to_string(m_numerical->get_index()) + ")";
}

std::shared_ptr<const BaseCondition> EqualNumericalCondition::visit(PolicyBuilder& policy_builder) const {
    return policy_builder.add_eq_condition(policy_builder.add_numerical_feature(*m_numerical));
}


GreaterNumericalCondition::GreaterNumericalCondition(std::shared_ptr<const core::Numerical> numerical_feature)
    : NumericalCondition(numerical_feature) { }

bool GreaterNumericalCondition::evaluate(const core::State& source_state, evaluator::EvaluationCache& cache) const {
    return cache.retrieve_or_evaluate(*m_numerical, source_state) > 0;
}

std::string GreaterNumericalCondition::compute_repr() const {
    return "(:c_n_gt " + std::to_string(m_numerical->get_index()) + ")";
}

std::shared_ptr<const BaseCondition> GreaterNumericalCondition::visit(PolicyBuilder& policy_builder) const {
    return policy_builder.add_gt_condition(policy_builder.add_numerical_feature(*m_numerical));
}

}
