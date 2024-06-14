import argparse
import os
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Width 0 shortcut")
    parser.add_argument("domain")
    parser.add_argument("feature_pool", choices=["dlplan", "wlplan"])
    parser.add_argument("-e", "--encoding", choices=["d2", "explicit", "expressivity"], type=str, default="expressivity")
    parser.add_argument("-w", "--workspace", default="workspace")
    args = parser.parse_args()

    domain_pddl = f"learning/benchmarks/{args.domain}/domain.pddl"
    instances_dir = f"learning/benchmarks/{args.domain}/instances"

    assert os.path.exists(domain_pddl), domain_pddl
    assert os.path.exists(instances_dir), instances_dir

    domain_pddl = os.path.abspath(domain_pddl)
    instances_dir = os.path.abspath(instances_dir)

    cmd = [
        "python3",
        "main.py",
        "--domain_filepath",
        domain_pddl,
        "--problems_directory",
        instances_dir,
        "--width",
        "0",
        "--workspace",
        os.path.abspath(args.workspace),
        "--encoding_type",
        args.encoding,
        "--feature_pool",
        args.feature_pool,
    ]

    subprocess.check_call(cmd, cwd="learning")
