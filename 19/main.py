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


def matches_patterns(pattern, towels, *, iter=-1):

    # print( "-----" *iter if iter>0 else "" , "PATTERN", pattern, towels)
    
    
    for t in towels:
        if pattern ==t:
            return True
        if pattern.startswith(t):
            rest = pattern[ len(t): ]
            # print(t, "REST",rest)
            res = matches_patterns(rest, towels, iter= iter+1 if iter>0 else -1)
            if res == True:
                return True

    return False


def main():

    # --- read data
    data = read_input(INPUT_FILE)
    # lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    tws,pts =read_towels(data)

    print(tws,pts)

    
    res = 0
    for p in pts:
        if matches_patterns(p,tws):
            res +=1
        # else:
            # print(p,tws)

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
