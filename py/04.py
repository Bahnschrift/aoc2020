import math as M
import collections as C
import bahnslib as B


def part_1(data):
    return sum(map(lambda entry: len(entry) == 8 or (len(entry) == 7 and "cid" not in entry), [B.str_dict(" ".join(x)) for x in B.split(data, "")]))


def part_2(data):
    valid = lambda entry: (
        len(entry) == 8 or (len(entry) == 7 and "cid" not in entry)) and (
        1920 <= int(entry["byr"]) <= 2002) and (
        2010 <= int(entry["iyr"]) <= 2020) and (
        2020 <= int(entry["eyr"]) <= 2030) and (
        entry["hgt"][-2:] == "cm" and 150 <= int(entry["hgt"][:-2]) <= 193 or entry["hgt"][-2:] == "in" and 59 <= int(entry["hgt"][:-2]) <= 76) and (
        entry["hcl"][0] == "#" and len(entry["hcl"][1:]) == 6 and all([x in "1234567890abcdefABCDEF" for x in entry["hcl"][1:]])) and (
        entry["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")) and (
        len(entry["pid"]) == len([x for x in entry["pid"] if x.isdigit()]) == 9)

    return sum(map(valid, [B.str_dict(" ".join(x)) for x in B.split(data, "")]))

if __name__ == "__main__":
    import runner.runner as runner
    x = B.ints(__file__)[-1]
    runner.run(day=x)