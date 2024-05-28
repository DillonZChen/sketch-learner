import logging

LOGGER = logging.getLogger(__name__)


def print_mat(mat: list[list], rjust: bool = True):
    if not mat:
        LOGGER.warning("Empty matrix")
        return

    max_lengths = [max(len(str(row[i])) for row in mat) for i in range(len(mat[0]))]

    for row in mat:
        ret = ""
        for i, cell in enumerate(row):
            if rjust:
                ret += str(cell).rjust(max_lengths[i]) + "  "
            else:
                ret += str(cell).ljust(max_lengths[i]) + "  "
        LOGGER.info(ret)


def read_log(log_text):
    text = log_text[log_text.find("Resulting minimized sketch:") :]
    lines = text.split("\n")

    data = {}

    for line in lines:
        if line.startswith("Numer of sketch rules"):
            data["rules"] = int(line.split()[-1].strip())
        elif line.startswith("Number of selected features"):
            data["features"] = int(line.split()[-1].strip())
        elif line.startswith("Maximum complexity of selected feature"):
            data["complexity"] = int(line.split()[-1].strip())
        elif line.startswith("Preprocessing time"):
            data["preprocessing"] = float(line.split()[-2].strip())
        elif line.startswith("ASP time"):
            data["asp"] = float(line.split()[-2].strip())
        elif line.startswith("Verification time"):
            data["verification"] = float(line.split()[-2].strip())
        elif line.startswith("Total time"):
            data["total"] = float(line.split()[-2].strip())

    return data
