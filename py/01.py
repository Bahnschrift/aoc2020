import math as M
import collections as C
import bahnslib as B
from itertools import combinations

def part_1(data):
    data = map(int, data)
    c = combinations(data, 2)
    for x in c:
        if sum(x) == 2020:
            return x[0] * x[1]
    
def part_2(data):
    data = map(int, data)
    c = combinations(data, 3)
    for x in c:
        if sum(x) == 2020:
            return x[0] * x[1] * x[2]


if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)