s = open("08.ipynb").read()
for x in range(9, 26):
    open(f"{str(x).zfill(2)}.ipynb", "w+").write(s.replace("day = 8", "day = " + str(x)).replace("Day 8", "Day " + str(x)))