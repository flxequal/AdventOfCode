
import time

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
125 17
"""

lookup = dict()

def blink(input, max_iter):

    updated = max_iter-1
    num_of_stones = 1

    if  0 == max_iter:
        return num_of_stones

    if lookup.get((input,max_iter),None):
        return lookup.get((input,max_iter))

    if input == 0:
        num_of_stones = blink(1, updated)

    elif len(str(input))%2 == 1:
        num_of_stones = blink(input *2024, updated)

    elif len(str(input))%2 == 0:
        l = len(str(input))
        stones_left = blink(int(str(input)[:(l//2)]), updated)
        stones_right = blink(int(str(input)[(l//2):]), updated)
        num_of_stones = stones_left + stones_right

    lookup[(input,max_iter)] = num_of_stones
    return num_of_stones



def main():

    start = time.time()
    iterations =75
    lines = read_input_as_lines(INPUT_FILE)
    res = 0
    line = [c for c in lines[0].split(" ")]

    times = []

    for c in line:


        t = time.time()
        res += blink(int(c), iterations)
        times.append(time.time()-t)

    print(time.time()-start)
    print(res)

    print(NEW_LINE.join(str(t) for t in times))

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
