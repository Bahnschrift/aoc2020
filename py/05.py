import math as M
import collections as C
import bahnslib as B
from itertools import combinations


def part_1(data):
    return max(int(line.translate("".maketrans("FBLR","0101")), 2) for line in data)


def part_2(data):
    ids = sorted(int(line.translate("".maketrans("FBLR","0101")), 2) for line in data)
    for x in range(1, len(ids)):
        if ids[x] - ids[x - 1] == 2:
            return ids[x] - 1


if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)