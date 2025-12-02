
import matplotlib.pyplot as plt
from collections import namedtuple
import re

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


parse_position = re.compile(r"(?<=p=)[-]?\d+,[-]?\d+")
parse_velocity = re.compile(r"(?<=v=)[-]?\d+,[-]?\d+")

Robot = namedtuple("Robot", ["px","py","vx","vy"] )

def walk (r:Robot, max_x:int, max_y :int, seconds: int) -> tuple[int,int] :

    new_position_x = r.px
    new_position_y = r.py 

    for i in range(seconds):

        new_position_x += r.vx
        new_position_y += r.vy

        if new_position_x >= max_x:
            new_position_x -= max_x
        elif new_position_x < 0:
            new_position_x += max_x

        if new_position_y >= max_y:
            new_position_y -= max_y
        elif new_position_y < 0:
            new_position_y += max_y

    return (new_position_x,new_position_y)

def find_full_neighbors(x,y,positions):
    return (x+1,y) in positions  and (x,y+1) in positions and (x-1,y) in positions and (x,y-1) #in positions and (x+1,y+1) in positions and (x+1,y-1) in positions and (x-1,y-1) in positions and (x-1,y+1) in positions

def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    r = Robot(2,4,2,-3)

    max_x,max_y = 101,103

    robots = []

    for line in lines:
        p = [ int(a) for a in parse_position.findall(line)[0].split(",")]
        v = [ int(a) for a in parse_velocity.findall(line)[0].split(",")]

        robots.append(Robot(p[0],p[1],v[0],v[1]))

    positions = []


    buffer = [[" " for _ in range( max_x)] for _ in range(max_y)]

    py_vars = []
    px_vars = []


    
    for s in range(20000):

        positions = []
        buffer = [[" " for _ in range( max_x)] for _ in range(max_y)]

        new_robots = []

        full_neighbours = 0

        for r in robots: 
            np = walk(r,max_x,max_y,1)
            new_robots.append(Robot(np[0],np[1],r.vx,r.vy))
            positions.append(np)

        for r in robots:
            if find_full_neighbors(r.px,r.py, positions):
                full_neighbours += 1

        robots = new_robots

        if full_neighbours>2:
            print(s,full_neighbours)


        if s in []: # enter seconds to stop and show the image
            for p in positions:
                buffer[p[1]][p[0]]="#"

            buff = NEW_LINE.join([ "".join(line) for line in buffer])
            print(buff)
            print(s)
            input("press enter")



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
