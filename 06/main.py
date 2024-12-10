

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
    trace.add(guard_start)
    guard_postition = guard_start

    while True:
        next_pos = move(guard_postition,direction)

        td = tuple([guard_postition[0],guard_postition[1]])

        if not (next_pos[0]>=0 and next_pos[0]<i_max and next_pos[1] >=0 and next_pos[1]<j_max):
            break

        if next_pos in obstacles:
            direction = next_direction(direction)
            continue

        guard_postition = next_pos
        trace.add(next_pos)


    print(len(trace))
# =======
#
# def main():
#
#     # --- read data
#     data = read_input(INPUT_FILE)
#     lines = read_input_as_lines(INPUT_FILE)
#
#     # --- sample data 
#     # data = SAMPLE
#     # lines = input_to_lines(SAMPLE)
#     grid = read_grid(data)
#
#     directions = ( (1,0), (0,-1),(-1,0),(0,1)  )
#     dir_i = 2
#
#
#     i_max= len(grid)
#     j_max= len(grid[0])
#
#     print(i_max,j_max)
#
#     guard_position = [0,0]
#     guard_direction = directions[dir_i]
#
#     guard_trace = {(guard_position[0],guard_position[1])}
#
#     for i,row in enumerate(grid):
#         for j, cell in enumerate(row):
#             if cell == "^":
#                 guard_position[0]=i
#                 guard_position[1]=j
#
#     print(guard_position)
#
#     in_grid = lambda pos : (pos[0]>=0 and pos[1]>=0) and (pos[0]<i_max and pos[1]<j_max)
#     move_step = lambda pos,dir: [ p+d  for p,d in zip(pos,dir) ]
#
#     # for _ in range(20):
#     while True :
#         guard_position = move_step(guard_position,guard_direction)
#         look_ahead = move_step(guard_position, guard_direction)
#         if not in_grid(look_ahead):
#             break
#         next = grid[look_ahead[0]][look_ahead[1]]
#         guard_trace.add(tuple(guard_position))
#         if next == "#":
#             # print("### obstacle at ", look_ahead)
#             dir_i+=1
#             guard_direction = directions[dir_i%4]
#             # print("new direction", guard_direction)
#
#     # print(guard_trace)
#     print(len(guard_trace))
#
#
#     result = 0
#
#
#     # C O D E
#
#     # print(result)
#
# >>>>>>> 97241bb (initial commit)


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
