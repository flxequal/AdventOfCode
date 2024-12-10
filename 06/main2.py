
import time

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

def read_grid(input):
    lines = input.split(NEW_LINE)
    return [ [c for c in l]  for l in lines if l]


def next_direction(dir):
    if dir == (1,0):
        return (0,-1)

    elif dir == (0,-1):
        return (-1,0)

    elif dir == (-1,0):
        return (0,1)

    elif dir == (0,1):
        return (1,0)
    else :
        raise Exception()

def move(pos,dir):
    a = pos[0]+dir[0]
    b = pos[1]+dir[1]
    return tuple([a,b])



def main():

    # --- read data
    data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # data = SAMPLE

    grid = read_grid(data)

    obstacles = set()

    i_max = len(grid)
    j_max = len(grid[0])

    for i, row in enumerate(grid):
        for j,cell in enumerate(row):
            if cell == "#":
                obstacles.add((i,j))
            if cell == "^":
                guard_start = (i,j)

    direction = (-1,0)

    trace = set()
    trace_dir = set()
    trace.add(guard_start)
    # trace_dir.add(tuple([guard_start[0],guard_start[1],direction[0],direction[1]]))

    new_obstacles = set()

    guard_postition = guard_start

    for i, row in enumerate(grid):
        print(i)
        for j,cell in enumerate(row):
            if cell == ".":
                obstacles.add((i,j))
            else:
                continue

            trace_dir = set()
            direction = (-1,0)
            guard_postition = guard_start
            while True:
                next_pos = move(guard_postition,direction)

                td = tuple([guard_postition[0],guard_postition[1],direction[0],direction[1]])

                if td in trace_dir:
                    print("LOOP",td)
                    new_obstacles.add(tuple([i,j]))
                    break
                trace_dir.add(td)
                if not (next_pos[0]>=0 and next_pos[0]<i_max and next_pos[1] >=0 and next_pos[1]<j_max):
                    break

                if next_pos in obstacles:
                    direction = next_direction(direction)
                    continue

                guard_postition = next_pos
                trace.add(next_pos)

            if cell == ".":
                obstacles.remove((i,j))
        # trace_dir.add(tuple([next_pos[0],next_pos[1],direction[0],direction[1]]))

    print(len(new_obstacles))
    # --- sample data 



# --- common helper functions ---

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
