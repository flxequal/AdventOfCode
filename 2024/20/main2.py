import re
import cProfile
from collections import namedtuple
import cmath

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

INF = 10e16

Node = namedtuple("Node",["pos"])
Entry = namedtuple("Entry",["node","cost","pre"])

def read_maze (input):
    walls = set()
    paths = set()
    reindeer = None
    end = None
    filtered_field = [line for line in input.split(NEW_LINE) if line]
    for i ,line in enumerate(filtered_field):
        for j, cell in enumerate(line):
            if cell == "#":
                walls.add((i,j))
            elif cell == "S":
                reindeer = (i,j)
            elif cell == "E":
                end = (i,j)
            elif cell == ".":
                paths.add((i,j))
    return walls,paths, reindeer,end



def pos_in_range(pos,steps,max_i,max_j) -> set[tuple[int,int]]:
    positions = set()
    dirs = [(k,l) for k in [-1,1] for l in [-1,1]]

    for i in range(steps+1):
        for j in range(steps-i+1):
            for d in dirs:
                pi = pos[0] + d[0]*i
                pj = pos[1] + d[1]*j
                positions.add((pi,pj))

    return positions



def calc_path(race_track,start:Node,end:Node):

    pre = None
    n = start 

    dist = 0

    path = dict()

    visited = set()

    while not n == end:
        p = n.pos
        directions  = [(1,0),(0,1),(-1,0),(0,-1)]

        for d in directions:
            new_i = p[0] + d[0]
            new_j = p[1] + d[1]

            if ((new_i,new_j)== end.pos or (new_i,new_j) in race_track) and not Node((new_i,new_j)) in visited:
                path[Node(p)]=(Entry(Node(p),dist,pre))
                dist += 1
                visited.add(Node(p))
                pre = n
                n = Node((new_i,new_j))
                break

    path[end] = Entry(end,dist,pre)

    return path
                


        
def dist_manhattan(a,b):


    return abs(b[0] - a[0]) + abs(b[1] -a[1])

def main():

    # --- read data
    data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    walls, race_track,start, end = read_maze(data)
    max_i, max_j =len(lines), len(lines[0])
    path = calc_path(race_track,Node(start),Node(end))


    # buffer = [ ["." for j in range(max_j)] for i in range(max_i) ]
    # for w in walls:
    #     i,j = w[0],w[1]
    #     buffer[i][j]="#"


    all_cheats = dict()
    node  = Node(end)
    while node:
        entry = path.get(node)
        positions = pos_in_range( node.pos,20,max_i,max_j )
        for p in positions:
            if path.get(Node(p)):
                other_node = path.get(Node(p))
                time_cheat = entry.cost - other_node.cost - dist_manhattan(node.pos, p)
                if time_cheat < 50:
                    continue
                t = all_cheats.get(time_cheat,0)
                all_cheats[time_cheat] = t+1
        del path[node]
        node = entry.pre
    res=0
    for c,t in all_cheats.items():
        if c>=100:
            res +=t

    # print(NEW_LINE.join([ "".join(row) for row in buffer ]))
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

def main_profile():

    cProfile.run("main()")

if __name__ == "__main__":
    main_profile()
    # main()
