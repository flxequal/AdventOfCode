import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


Machine = namedtuple("Machine",[ "ax" , "ay", "bx" , "by" , "prize_x", "prize_y" ])

find_x = re.compile(r"(?<=X\+)\d+")
find_y = re.compile(r"(?<=Y\+)\d+")

find_x_prize = re.compile(r"(?<=X=)\d+")
find_y_prize = re.compile(r"(?<=Y=)\d+")

def det (a,b,c,d):
    return a*d - c*b

def main():

    data = read_input(INPUT_FILE)
    res = 0 
    tokens_A = 3
    tokens_B = 1
    machine_data = [ m.strip() for m in data.split(NEW_LINE + NEW_LINE)]
    machines = []

    for block in machine_data:
        ba,bb, prize = block.split(NEW_LINE,3)
        ax = find_x.findall(ba)[0]
        ay = find_y.findall(ba)[0]
        bx = find_x.findall(bb)[0]
        by = find_y.findall(bb)[0]
        px = int(find_x_prize.findall(prize)[0] )+ 10000000000000
        py = int(find_y_prize.findall(prize)[0] )+ 10000000000000
        machine = Machine(int(ax), int(ay),int(bx),int(by),int(px),int(py))
        machines.append(machine)

    for m in machines:
        det_1 = det (m.ax, m.bx, m.ay,m.by)
        det_2 = det(m.prize_x,m.bx,m.prize_y,m.by)
        det_3 = det(m.ax,m.prize_x,m.ay,m.prize_y)
        A = det_2/det_1
        B = det_3/det_1
        is_valid = A.is_integer() and B.is_integer()
        if is_valid :
            res += A * tokens_A
            res += B * tokens_B

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
