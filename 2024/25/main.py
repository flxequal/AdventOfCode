import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


def locks_and_keys_from_data(data):
    blocks = data.split(NEW_LINE*2)

    locks = []
    keys = []
    
    for i,b in enumerate(blocks):
        stripped = b.strip()
        print(i, b.strip()[:5])
        if stripped[:5] == "#"*5:
           print("key",stripped) 
           print(read_topo(stripped))
           keys.append(read_topo(stripped))
        elif stripped[:5] == "."*5:
           locks.append(read_topo(stripped))
           print("lock")
           print(read_topo(stripped))
    return locks, keys

def read_topo(data):
    
    lines = data.split(NEW_LINE)
    topo = [-1 for _ in range(5)]
    for l in lines:
        for i,c in enumerate(l):
            if c == "#":
                topo[i] += 1
    return topo




def main():

    # --- read data
    data = read_input(INPUT_FILE)
    # lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    


    lines = input_to_lines(SAMPLE)

    locks, keys = locks_and_keys_from_data(data)

    res = 0

    for lock in locks:
        for key in keys:
            if all([(l+k)<6 for l,k in zip(lock,key)]):
                res +=1

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
