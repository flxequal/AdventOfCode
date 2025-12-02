import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def read_towels (data):

    towels , patterns = data.split(NEW_LINE+NEW_LINE)
    towels = [t.strip() for t in towels.split(",")]
    patterns = [p.strip() for p in patterns.split(NEW_LINE) if p]
    return (towels,patterns)


def matches_patterns(pattern, towels,cache, *, iter=-1):


    counter = 0
    found = False

    if len(pattern) == 0:
        return (True,1,cache)

    if pattern in cache:
        f,c = cache[pattern]
        return f,c,cache
    
    for t in towels:
        if pattern.startswith(t):
            rest = pattern[ len(t): ]
            f,c, r_cache = matches_patterns(rest, towels,cache, iter= iter+1 if iter>0 else -1)
            cache[rest] = (f,c)
            cache.update(r_cache)
            if f == True:
                found = True
                counter += c

    if found:
        return (True, counter,cache)


    return (False ,0,cache)


def main():

    # --- read data
    data = read_input(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE

    tws,pts =read_towels(data)

    res = 0
    cache = dict()

    for _,p in enumerate(pts):
        _,c,ca= matches_patterns(p,tws,cache,iter=1)
        cache.update(ca)
        res +=c
    
    print(res)


# --- common helper functions ---


def val_positions_in_grid (val, grid):

    res = []
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == val:
                res.append((i,j))
    return res

def read_input(file_name):
    with open (file_name,"r") as fp:
        data = fp.read()
        return data

def input_to_lines(input):
    return [ line for line in input.split(NEW_LINE) if line.strip()]

def read_input_as_lines(input_file):
    data = read_input(input_file)
    return input_to_lines(data)


if __name__ == "__main__":
    main()
