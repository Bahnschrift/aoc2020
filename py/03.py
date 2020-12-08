import math as M
import collections as C
import bahnslib as B


def part_1(data, right=3, down=1):
    x, y = 0, 0
    t = 0
    for i in range(len(data) // down - 1):
        x += right
        x = x % len(data[i])
        y += down
        if data[y][x] == "#":
            t += 1
    return t

    
def part_2(data):
    return part_1(data, right=1, down=1) * part_1(data, right=3, down=1) * part_1(data, right=5, down=1) * part_1(data, right=7, down=1) * part_1(data, right=1, down=2)


if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)