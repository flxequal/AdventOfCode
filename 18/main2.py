import re
from collections import namedtuple, deque

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

INF = 10e20

def build_graph( memory, corrupted):
    graph =dict()
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for m in memory:
        if m in corrupted:
            continue
        edges = graph.get(m,dict())
        for d in directions:
            ni = m[0] + d[0]
            nj = m[1] + d[1]

            if (ni,nj) in memory and not (ni,nj) in corrupted:
                edges[(ni,nj)] = 1

        if len(edges)>0:
            graph[m] = edges
    return graph


Cell = namedtuple("Cell", ["pos","g","h","prev"])

def dist_manhattan(a,b):
    return abs(b[0] - a[0]) + abs(b[1] -a[1])

def a_star(start,end, graph):
        
    de = set([Cell(start, 0 , dist_manhattan(start,end),None)])
    visited = dict()
    final_cell = None

    while True:

        f = INF 
        next_cell : Cell = Cell(None,None,None,None)

        if len(de) == 0:
            print("FAILED")
            return None

        for cell in de.copy():
            next_cell = cell if cell.g + cell.h < f else next_cell
            f = cell.g + cell.h if cell.g + cell.h < f else f
        de.remove(next_cell)
        visited[next_cell.pos] = next_cell

        if next_cell.pos == end:
            final_cell = next_cell
            break
        else:
            edges = graph.get(next_cell.pos,[])
            for edge_node ,dist in edges.items():

                if not edge_node in visited:
                    de.add( Cell(edge_node, dist+next_cell.g , dist_manhattan(edge_node,end),next_cell.pos)  )

    path = [final_cell.pos]
    next_cell = final_cell.pos

    while True:
        vsted = visited.get(next_cell,None)
        if not vsted:
            return path
        if vsted.prev:
            path.append(vsted.prev)
        next_cell = vsted.prev

def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)
    max_i, max_j = 71,71
    num_bytes = 1024

    # --- sample data 
    # lines = input_to_lines(SAMPLE)
    # max_i, max_j = 7,7
    # num_bytes = 12

    corrupted = []
    for line in lines:
        a,b = line.split(",")
        corrupted.append((int(a),int(b)))

    memory = {(i,j) for j in range(max_j) for i in range(max_i)}

    g = build_graph(memory,corrupted[:num_bytes])
    path = a_star((0,0),(max_i-1,max_j-1),g)

    for i in range(num_bytes,len(corrupted)):
        byte = corrupted[i]
        print(f"ADD {byte} after {i}ns")
        if not byte in path:
            continue
        else:
            g = build_graph(memory,corrupted[:i+1])
            path = a_star((0,0),(max_i-1,max_j-1),g)
            if not path:
                print("FAILED AT",i,byte)
                break

    # buffer = [ ["." for j in range(max_j)] for i in range(max_i) ]
    # print(NEW_LINE.join([ "".join(row) for row in buffer ]))


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
