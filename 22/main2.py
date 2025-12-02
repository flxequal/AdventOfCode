import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
1
2
3
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
    buyers = []
    # for line in ["123"]:
    for line in lines:
        secret = int(line)
        prices = [secret % 10]
        for _ in range(2000):
            secret = next_secret_number(secret)
            prices.append(secret %10)
        buyers.append(prices)

    # print(buyers)

    buyers_lookup = []
    for prices in buyers:
        local_lookup = dict()
        for i in range(5, len(prices)):
            window = prices[i-5:i]
            sequence = tuple(window[i] - window[i-1] for i in range(1, len(window)))
            if not sequence in local_lookup:
                local_lookup[sequence]=window[-1]
        buyers_lookup.append(local_lookup)


    # print(buyers_lookup)

    possible_sequences = set()

    for lookups in buyers_lookup:
        possible_sequences.update(lookups.keys())

    # print(possible_sequences)

    best = 0

    best_seq = None

    lll = len(possible_sequences)
    i=0

    for seq in possible_sequences:
        tmp_res = 0
        # print(lll-i)
        i+=1
        # print(seq)
        for lookup in buyers_lookup:
            tmp_res += lookup.get(seq,0)
            # print(tmp_res)
        if tmp_res > best:
            best = tmp_res
            best_seq = seq

    print(best, best_seq)

            
            






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
