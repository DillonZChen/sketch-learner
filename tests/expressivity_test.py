""" test whether original configurations with symmetry preserves outputs """

import datetime
import logging
import os
import subprocess
import sys
import threading

import pytest
from kr_submission_data import DOMAINS
from util import print_mat, read_log

LOGGER = logging.getLogger(__name__)

SHORT = ["blocks_4_clear", "gripper", "spanner"]
MEDIUM = ["blocks_4_clear", "blocks_4_on", "ferry", "gripper", "miconic", "reward", "spanner"]
LONG = sorted(list(DOMAINS))

DOMAINS_TO_TEST = SHORT
TIMEOUT = 60

@pytest.mark.parametrize("domain_name", DOMAINS_TO_TEST)
def test_expressivity(domain_name):
    domain_path = f"learning/benchmarks/{domain_name}/domain.pddl"
    problems_dir = f"learning/benchmarks/{domain_name}/instances"
    os.makedirs(f"workspaces/tests", exist_ok=True)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    workspace_path = f"workspaces/tests/{domain_name}" + f"_{current_time}"
    cmd = [
        "python3",
        "learning/main.py",
        "--domain_filepath",
        domain_path,
        "--problems_directory",
        problems_dir,
        "--width",
        "0",
        f"--workspace",
        f"{workspace_path}",
        "--encoding_type",
        "expressivity",
    ]
    LOGGER.info(f"Running command:\n{' '.join(cmd)}")

    def run_command(cmd):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, error = process.communicate(timeout=TIMEOUT)
            return output.decode("utf-8")
        except subprocess.TimeoutExpired:
            process.kill()
            output, error = process.communicate()
            LOGGER.info(f"Timeout of {TIMEOUT} seconds reached.")
            assert False

    output = run_command(cmd)
    with open(f"{workspace_path}/run.log", "w") as f:
        f.write(output)
    data = read_log(output)
    LOGGER.info(f"{data}")

    LOGGER.info("Notes: number of sketch rules is nondeterministic. Minisation is over sum of feature complexities so these may also be nondeterministic...")
    mat = [["key", "pred", "true"]]
    for k in ["rules", "features", "complexity"]:
        mat.append([k, data[k], DOMAINS[domain_name][k]])
    print_mat(mat)
    # for k in ["features", "complexity"]:
    #     assert data[k] == DOMAINS[domain_name][k]
