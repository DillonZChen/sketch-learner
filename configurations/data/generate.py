DOMAINS = [
    "barman",
    "blocks_3",
    "blocks_4",
    "blocks_4_clear",
    "blocks_4_on",
    "childsnack",
    "delivery",
    "driverlog",
    "ferry",
    "grid",
    "gripper",
    "hiking",
    "logistics",
    "miconic",
    "reward",
    "rovers",
    "satellite",
    "spanner",
    "visitall",
]

TEMPLATE = r"""
[training]
domain_pddl = '<DOMAIN_PDDL>'
tasks_dir = '<TASKS_DIR>'
"""

for domain in DOMAINS:
    text = TEMPLATE[1:]
    text = text.replace("<DOMAIN_PDDL>", f"learning/benchmarks/{domain}/domain.pddl")
    text = text.replace("<TASKS_DIR>", f"learning/benchmarks/{domain}/instances")
    with open(f"{domain}.toml", "w") as f:
        f.write(text)
