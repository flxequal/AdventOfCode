

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
125 17
"""

lookup = dict()

def blink(input, max_iter):
    if  0 == max_iter:
        return 1
    if input == 0:
        return blink(1,max_iter-1)
    elif len(str(input))%2 == 1:
        new_input = input * 2024
        return blink(new_input, max_iter-1)
    elif len(str(input))%2 == 0:
        l = len(str(input))
        a = int(str(input)[:(l//2)])
        b = int(str(input)[(l//2):])
        ba = blink(a, max_iter-1)
        bb = blink(b, max_iter-1)
        lookup[input] = ba+bb
        return bb+ba



def main():

    lines = read_input_as_lines(INPUT_FILE)
    line = [c for c in lines[0].split(" ")]
    res = 0

    for c in line:
        res += blink(int(c),25)

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
