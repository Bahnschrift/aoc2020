import math as M
import collections as C
import bahnslib as B


def part_1(data):
    g = 0
    for x in data:
        mi, ma = map(int, x.split()[0].split('-'))
        char = x.split()[1][0]
        s = x.split()[2]
        if mi <= s.count(char) <= ma:
            g += 1
    return g
    
def part_2(data):
    g = 0
    for x in data:
        mi, ma = map(int, x.split()[0].split('-'))
        char = x.split()[1][0]
        s = x.split()[2]
        if (s[mi - 1] == char and s[ma - 1] != char) or (s[mi - 1] != char and s[ma - 1] == char):
            g += 1
    return g


if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)