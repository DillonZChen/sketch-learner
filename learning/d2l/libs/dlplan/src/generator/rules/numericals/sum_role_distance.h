#ifndef DLPLAN_SRC_GENERATOR_RULES_NUMERICALS_SUM_ROLE_DISTANCE_H_
#define DLPLAN_SRC_GENERATOR_RULES_NUMERICALS_SUM_ROLE_DISTANCE_H_

#include "../numerical.h"

namespace dlplan::generator::rules {

class SumRoleDistanceNumerical : public Numerical {
public:
    SumRoleDistanceNumerical() : Numerical("n_sum_role_distance") { }

    virtual void submit_tasks_impl(const States& states, int iteration, GeneratorData& data, utils::threadpool::ThreadPool& th) override {
        core::SyntacticElementFactory factory = *data.m_factory;
        for (int i = 1; i < iteration; ++i) {
            for (int j = 1; j < std::max(2,iteration - i); ++j) {
                int k = iteration - i - j;
                for (const auto& r1 : data.m_roles_by_iteration[i]) {
                    for (const auto& r2 : data.m_roles_by_iteration[j]) {
                        for (const auto& r3 : data.m_roles_by_iteration[k]) {
                            m_tasks.push_back(th.submit(std::cref(m_task), std::cref(states), std::move(factory.make_sum_role_distance(r1, r2, r3))));
                        }
                    }
                }
            }
        }
    }
};

}

#endif
