

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

def walk_trail(i,j, grid):
    val=0

    if grid[i][j]!=".":
        val = int(grid[i][j])
    else:
        val = -10000

    res = set()

    for d in [(1,0),(0,1),(-1,0),(0,-1)] :

        inew = i+d[0]
        jnew = j+d[1]

        if inew < len(grid) and inew>=0 and jnew<len(grid) and jnew >=0 :
            if grid[inew][jnew] == ".":
                continue
            v = int(grid[inew][jnew])
            if v == 9 and (v-val)==1:
                res.add((inew,jnew))
            elif v != 9 and (v-val)==1:
                n= walk_trail(inew,jnew,grid)
                res.update(n)
    return res


def main():

    rows= read_input_as_lines(INPUT_FILE)
    start_positions = val_positions_in_grid("0",rows)
    result = 0

    for p in start_positions:
        r=  walk_trail(p[0],p[1], rows)
        result += len(r)

    print(result)



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
