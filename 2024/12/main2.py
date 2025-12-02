
import random

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

def rand_color_printer():
    i = random.randint(1,231)
    def foo(c):
        return f"\033[38;5;{i}m{c}\033[0m"
    return foo


SAMPLE="""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

# SAMPLE="""
# AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA
# """

def find_area(i,j, grid):
    value = grid[i][j]
    i_max = len(grid)
    j_max = len(grid[0])

    area = {(i,j)}
    new_fields = {(i,j)}
    next_fields = set()

    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    while len(new_fields)>0:
        for n in new_fields:
            ni = n[0]
            nj = n[1]

            for d in directions:
                new_i = ni+d[0]
                new_j = nj+d[1]

                i_in_range = ni+d[0]>=0 and ni+d[0] < i_max
                j_in_range = nj+d[1]>=0 and nj+d[1] < j_max

                if i_in_range and j_in_range:
                    if grid[new_i][new_j] == value:
                        if not (new_i ,new_j) in area :
                            area.add((new_i,new_j))
                            next_fields.add((new_i,new_j))

        new_fields = next_fields
        next_fields = set()

    return area

def calc_fence(area):

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    fences = list()

    for a in area:
        for d in directions:
            fi = a[0] + d[0]
            fj = a[1] + d[1]

            if not (fi,fj) in area:
                fences.append((fi,fj))

    return fences

    
def calc_lines(area, grid):

    i_min = min(a[0] for a in area)
    j_min = min(a[1] for a in area)

    i_max = max(a[0] for a in area)
    j_max = max(a[1] for a in area)

    grid_i_max= len(grid)
    grid_j_max= len(grid[0])

    origin = next(iter(area))

    v = grid[origin[0]][origin[1]]

    def in_bound(i,j):
        i_in =  i>=0 and i< grid_i_max
        j_in =  j>=0 and j< grid_j_max
        return i_in and j_in

    def get_value(i,j):
        if(i,j)in area:
            return grid[i][j]
        return None

    edges = 0

    for i in range(i_min,i_max+2):
        in_edge = False
        previous_direction=[]

        for j in range(j_min,j_max+2):

            upper_present = in_bound(i-1,j) and (get_value(i-1,j) == v)
            lower_present = in_bound(i,j) and (get_value(i,j) == v)

            edge_detected = upper_present != lower_present
            direction = [upper_present, lower_present]

            if direction != previous_direction:
                edge_flipped = True 
            else:
                edge_flipped = False
            
            if in_edge and edge_detected and edge_flipped:
                edges += 1
            elif (not in_edge) and edge_detected:
                edges += 1
                in_edge = True
            elif in_edge and (not edge_detected):
                in_edge = False

            previous_direction = direction

        if in_edge:
            edges += 1

    return  edges








def main():

    lines = read_input_as_lines(INPUT_FILE)
    grid = set()

    res = 0 

    for i,l in enumerate(lines):
        for j in range(len(l)):
            grid.add((i,j))

    areas = dict()

    while len(grid) > 0:
        cell =next(iter(grid))
        i,j = cell[0],cell[1]
        area = find_area(i,j,lines)
        v = lines[i][j]

        for c in area:
            grid.remove(c)

        ars =  areas.get(v,[])
        ars.append(area)
        areas[v] = ars

    res=0

    for _,v in areas.items():
        for a in v:
            r =calc_lines(a,lines)
            res += r *2 * len(a)

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
