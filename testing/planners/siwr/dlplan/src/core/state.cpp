#include "../../include/dlplan/core.h"

#include <algorithm>
#include <stdexcept>

#include "instance_info.h"
#include "../utils/collections.h"
#include "../utils/hash_utils.h"


namespace dlplan::core {

State::State(std::shared_ptr<const InstanceInfo> instance_info, const std::vector<Atom>& atoms)
    : m_instance_info(instance_info) {
    if (!std::all_of(atoms.begin(), atoms.end(), [&](const auto& atom){ return instance_info->exists_atom(atom); })) {
        throw std::runtime_error("State::State - atom does not exist in InstanceInfo.");
    }
    if (!std::all_of(atoms.begin(), atoms.end(), [&](const auto& atom){ return !atom.get_is_static(); })) {
        throw std::runtime_error("State::State - not allowed to pass static atoms because they are added automatically.");
    }
    m_per_predicate_idx_static_atom_idxs = instance_info->get_per_predicate_idx_static_atom_idxs();
    m_atom_idxs.reserve(atoms.size() + instance_info->get_static_atom_idxs().size());
    for (const auto& atom : atoms) {
        int atom_idx = atom.get_index();
        int predicate_idx = atom.get_predicate().get_index();
        m_atom_idxs.push_back(atom_idx);
        m_per_predicate_idx_static_atom_idxs[predicate_idx].push_back(atom_idx);
    }
    m_atom_idxs.insert(m_atom_idxs.end(), instance_info->get_static_atom_idxs().begin(), instance_info->get_static_atom_idxs().end());
}

State::State(std::shared_ptr<const InstanceInfo> instance_info, const Index_Vec& atom_idxs)
    : m_instance_info(instance_info) {
    const auto& atoms = instance_info->get_atoms();
    if (!std::all_of(atom_idxs.begin(), atom_idxs.end(), [&](int atom_idx){ return utils::in_bounds(atom_idx, atoms); })) {
        throw std::runtime_error("State::State - atom index out of range.");
    }
    if (!std::all_of(atom_idxs.begin(), atom_idxs.end(), [&](int atom_idx){ return !atoms[atom_idx].get_is_static(); })) {
        throw std::runtime_error("State::State - not allowed to pass static atoms because they are added automatically.");
    }
    m_per_predicate_idx_static_atom_idxs = instance_info->get_per_predicate_idx_static_atom_idxs();
    m_atom_idxs.reserve(atoms.size() + instance_info->get_static_atom_idxs().size());
    for (int atom_idx : atom_idxs) {
        const auto& atom = atoms[atom_idx];
        int predicate_idx = atom.get_predicate().get_index();
        m_atom_idxs.push_back(atom_idx);
        m_per_predicate_idx_static_atom_idxs[predicate_idx].push_back(atom_idx);
    }
    m_atom_idxs.insert(m_atom_idxs.end(), instance_info->get_static_atom_idxs().begin(), instance_info->get_static_atom_idxs().end());
}

State::State(const State&) = default;

State& State::operator=(const State&) = default;

State::State(State&& other) = default;

State& State::operator=(State&& other) = default;

State::~State() = default;

bool State::operator==(const State& other) const {
    return (get_atom_idxs() == other.get_atom_idxs()) && (get_instance_info() == other.get_instance_info());
}

bool State::operator!=(const State& other) const {
    return !(*this == other);
}

std::shared_ptr<const InstanceInfo> State::get_instance_info() const {
    return m_instance_info;
}

const Index_Vec& State::get_atom_idxs() const {
    return m_atom_idxs;
}

const phmap::flat_hash_map<int, std::vector<int>>& State::get_per_predicate_idx_static_atom_idxs() const {
    return m_per_predicate_idx_static_atom_idxs;
}


std::string State::str() const {
    std::string res("{");
    for (int i = 0; i < static_cast<int>(m_atom_idxs.size()); ++i) {
        const auto& atom = m_instance_info->get_atom(m_atom_idxs[i]);
        res += atom.str();
        if (i < static_cast<int>(m_atom_idxs.size()) - 1) {
            res += ", ";
        }
    }
    res += "}";
    return res;
}

size_t State::compute_hash() const {
    std::size_t seed = 0;
    utils::hashing::hash_combine(seed, std::hash<std::vector<int>>()(m_atom_idxs));
    utils::hashing::hash_combine(seed, m_instance_info);
    return seed;
}


}
