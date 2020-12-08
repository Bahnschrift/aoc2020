import math as M
import collections as C
import bahnslib as B


def part_1(data):
    return sum(len(set.union(*map(set,group))) for group in B.split(data, ""))
    # return sum(len(set("".join(x))) for x in B.split(data, ""))
    
def part_2(data):
    return sum(len(set.intersection(*map(set,group))) for group in B.split(data, ""))

if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)