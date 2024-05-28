from util import read_log

DOMAINS = {
    "blocks_3": {
        "rules": 5,
        "features": 3,
        "complexity": 7,
        "preprocessing": 765.0,
        "asp": 16973.0,
        "verification": 437.0,
        "total": 18173.0,
    },
    "blocks_4_clear": {
        "rules": 3,
        "features": 2,
        "complexity": 2,
        "preprocessing": 15.0,
        "asp": 2.0,
        "verification": 1.0,
        "total": 17.0,
    },
    "blocks_4_on": {
        "rules": 7,
        "features": 3,
        "complexity": 6,
        "preprocessing": 79.0,
        "asp": 236.0,
        "verification": 4.0,
        "total": 319.0,
    },
    "delivery": {
        "rules": 9,
        "features": 3,
        "complexity": 15,
        "preprocessing": 1008.0,
        "asp": 233.0,
        "verification": 176.0,
        "total": 1416.0,
    },
    "ferry": {
        "rules": 4,
        "features": 3,
        "complexity": 9,
        "preprocessing": 20.0,
        "asp": 76.0,
        "verification": 2.0,
        "total": 97.0,
    },
    "gripper": {
        "rules": 4,
        "features": 2,
        "complexity": 4,
        "preprocessing": 3.0,
        "asp": 1.0,
        "verification": 1.0,
        "total": 4.0,
    },
    "miconic": {
        "rules": 5,
        "features": 3,
        "complexity": 6,
        "preprocessing": 47.0,
        "asp": 32.0,
        "verification": 18.0,
        "total": 97.0,
    },
    "reward": {
        "rules": 2,
        "features": 2,
        "complexity": 6,
        "preprocessing": 32.0,
        "asp": 3.0,
        "verification": 32.0,
        "total": 66.0,
    },
    "spanner": {
        "rules": 3,
        "features": 2,
        "complexity": 9,
        "preprocessing": 8.0,
        "asp": 2.0,
        "verification": 1.0,
        "total": 10.0,
    },
    "visitall": {
        "rules": 3,
        "features": 2,
        "complexity": 7,
        "preprocessing": 1548.0,
        "asp": 1.0,
        "verification": 15192.0,
        "total": 16741.0,
    },
}

if __name__ == "__main__":
    for domain in DOMAINS:
        path = f"workspace-sym-2024-3-27/{domain}_0/run.log"
        with open(path) as f:
            text = f.read()
        data = read_log(text)
        data = repr(data).replace("}", ",}")
        print(f'"{domain}": {data},')
