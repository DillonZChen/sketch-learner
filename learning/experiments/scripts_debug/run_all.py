import os
import time

from tqdm import tqdm

scripts = [
    "blocks_3_0",
    "blocks_3_1",
    "blocks_3_2",
    "blocks_4_clear_0",
    "blocks_4_clear_1",
    "blocks_4_clear_2",
    "blocks_4_on_0",
    "blocks_4_on_1",
    "blocks_4_on_2",
    "delivery_0",
    "delivery_1",
    "delivery_2",
    "gripper_0",
    "gripper_1",
    "gripper_2",
    "miconic_0",
    "miconic_1",
    "miconic_2",
    "reward_0",
    "reward_1",
    "reward_2",
    "spanner_0",
    "spanner_1",
    "spanner_2",
    "visitall_0",
    "visitall_1",
    "visitall_2",
]

times = {}

os.system("rm -rf workspace")

for script in tqdm(scripts):
    t = time.time()
    os.system(f"./{script}.sh")
    times[script] = time.time() - t
