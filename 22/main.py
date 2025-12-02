import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
1
10
100
2024
"""


def next_secret_number(secret):
    secret =  (secret ^  (secret << 6)) % (1<<24)
    secret =  (secret ^  (secret >> 5)) % (1<<24)
    secret =  (secret ^  (secret << 11)) % (1<<24)
    return secret





def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    data = SAMPLE
    # lines = input_to_lines(SAMPLE)


    res = 0
    for line in lines:
        secret = int(line)
        for _ in range(2000):
            secret = next_secret_number(secret)
        res += secret 

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
