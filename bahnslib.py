from typing import Dict, Iterable, List, Any, Type, Union, Tuple
import re


"""
Takes an interable of strings and returns every single digit integer found, in order.

"th1s 1s 4n 3x4mp13" --> [1, 1, 4, 3, 4, 1, 3]
"""
def digits(it: Iterable[str]) -> List[int]:
    return [int(x) for x in it if x.isdigit()]



"""
Takes a string and finds all integers. Consecutive digits are treated as the same integer

th1s 1s 4n 3x4mp13" --> [1 ,1, 4, 3, 4, 13]
"""
def ints(it: str, type: Type=int) -> List[Any]:
    return [type(x) for x in re.split(r"\D+", it) if x.isdigit()]  # Split at non int characters, then convert to int. Conversion can create trailing "" so str.isdigit check



"""
Enforces a set row length on a 2 dimensional iterable. If no length is given, defaults to the max length row.
[
    [1, 2],
    [4, 5, 6],
    [11]
] 
 -->
[
    [1, 2, None],
    [4, 5, 6],
    [11, None, None]
]
"""
def pad_grid(grid: Iterable[Iterable[Any]], pad_value: Any=None, row_len: int=None) -> List[List[Any]]:
    max_len = len(max(*grid, key=len))
    if row_len is None:
        row_len = max_len

    if row_len < max_len:
        raise IndexError(f"Row length provided: {row_len} is less than max existing row length: {max_len}.")

    filled_grid = []
    for row in grid:
        new_row = list(row)
        new_row += [pad_value for x in range(row_len - len(new_row))]
        filled_grid.append(new_row)
    return filled_grid



"""
Takes a two dimensional grid, and returns the grid "rotated" 90degs clockwise, i.e. col 0 -> row 0, col 1 -> row 1, etc.

[
    [1, 2,  3 ],
    [4, 5,  6 ],
    [7, 8     ],
    [9, 10, 11]
] 
 -->
[
    [1, 4, 7,     9],
    [2, 5, 8,    10],
    [3, 6, None, 11]
]
"""
def as_cols(grid: Iterable[Iterable[Any]], pad_value: Any=None) -> List[List[Any]]:
    grid = pad_grid(grid, pad_value=pad_value)
    return [list(x) for x in zip(*grid)]



"""
Splits any iterable at a certain value, returning a 2 dimensional list


["line 1", "line 2", "", "line 4", "", "line 6]


"""
def split(thing: Iterable, value: Any) -> List[List[Any]]:
    out = []
    new = []
    for item in thing:
        if item == value:
            out += [new]
            new = []
        else:
            new += [item]
    if new:  # Prevents trailing empty lists if initial iterable ended with the target value
        out += [new]
    return out


"""
Splits an iterable of strings at a certain value, returning a list of strings

["line 1", "line 2", "", "line 4", "", "line 6] -->
["line 1!line 2!line 3", "line4", "line6"]

"""
def split_join(thing: Iterable[str], value: str, join_with: str) -> List[str]:
    out = []
    new = []
    for item in thing:
        if item == value:
            out += [join_with.join(new)]
            new = []
        else:
            new += [item]
    if new:  # Prevents trailing empty lists if initial iterable ended with the target value
        out += [join_with.join(new)]
    return out



"""
Splits a string at a delimiter, then returns a dictionary of the resulting values, split by value and key at a separator character.


"hgt:68in byr:1933 iyr:2010 ecl:brn pid:380075958 hcl:#623a2f cid:279 eyr:2025"
 -->
{
    "hgt": "68in", 
    "byr": "1933", 
    "iyr": "2010", 
    "ecl": "brn", 
    "pid": "380075958", 
    "hcl": "#623a2f", 
    "cid": "279", 
    "eyr": "2025"
}
"""
def str_dict(in_str: str, delim=None, sep: str=":") -> Dict:
    return {x: y for x, y in [field.split(sep, maxsplit=1) for field in in_str.split(delim)]}


"""
Gets the advent of code input for a given day in a given year and checks if it is cached at the specified path. If not, then it grabs it from the website.
"""
def get_aoc_input(day: int, path: str, format: str="lines", year=2020) -> Union[str, list]:
    if format not in ("lines", "string"):
        raise LookupError("Format must be either 'lines' or 'string'")
    
    import requests
    
    file = open(path, "r+")
    contents = file.read()
    if contents == "":
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        id_file = open("../downloader/session_id.txt", "r")
        id = id_file.read().strip()
        id_file.close()
        cookies = {
            "session": id
        }
        r = requests.post(url, cookies=cookies, allow_redirects=True)
        file.write(r.text)
        
    file.close()
    file = open(path, "r")
    data = ""
    if format == "lines":
        data = [*map(str.rstrip, file.readlines())]
    elif format == "string":
        data = file.read().rstrip()
    file.close()
    return data

def yeet(*args):
    print("Yeet:", *args)


"""
Returns a list of tuples formed pairwise from an iterable. e.g.
[1, 2, 3, 4, 5] (size = 2) -> [(1, 2), (2, 3), (3, 4), (4, 5)]
[1, 2, 3, 4, 5] (size = 3) -> [[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
"""
def pairwise(arr: Union[str, List, Tuple], size: int=2) -> List[Tuple]:
    return [*zip(*[arr[x:x-size+1] for x in range(size - 1)], arr[size-1:])]