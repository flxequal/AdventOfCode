import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""


def read_field (input):
    field, commands = input.split(NEW_LINE+NEW_LINE)

    walls = set()
    boxes = set()
    robot = None
    filtered_field = [line for line in field.split(NEW_LINE) if line]
    print(field)

    for i ,line in enumerate(filtered_field):
        for j, cell in enumerate(line):
            if cell == "#":
                walls.add((i,j))
            elif cell == "O":
                boxes.add((i,j))
            elif cell =="@":
                robot = (i,j)
    
    return walls, boxes, robot

def read_commands(input):
    _ , commands = input.split(NEW_LINE+NEW_LINE)
    return [c for c in commands if c in ["<",">","^","v"]]




def apply_command(walls, boxes, robot, command):
    directions = { ">": (0,1), "<":(0,-1),"v":(-1,0),"^":(1,0) }
    d = directions.get(command)
    new_position= (robot[0] + d[0], robot[1]+d[1])

    boxes_to_move = []

    if new_position in walls :
        return
    if new_position in boxes:




def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    # lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    data = SAMPLE
    lines = input_to_lines(SAMPLE)



    walls, boxes, robot = read_field(data)

    print("WALLS",walls,"BOXES", boxes, robot)

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
