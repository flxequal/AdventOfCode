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

def dijkstra (graph,start):

    visited = set()
    Entry = namedtuple("Entry",["node","cost","pre"])
    lookup = dict()

    for k,_ in graph.items():
        if k != start:
            lookup[k]=Entry(k,INF,None)
        else:
            lookup[k]=Entry(k,0,k)

    print(lookup)
    current_nodes = [start]

    # while len(visited) != len(graph):
    for i in range(100000):

        new_node = None
        current_nodes = []
        for k,v in lookup.items():
            if not k in visited:
                if  INF > v.cost:
                    new_node = k

        if new_node:
            current_nodes.append(new_node)

        for cn in current_nodes:
            edges = graph.get(cn)
            for n, dist in edges.items():
                if n in visited:
                    continue
                current_node_entry = lookup[cn]
                foo = lookup[n]
                if foo.cost > dist+current_node_entry.cost:
                    lookup[n]=Entry(n,dist+current_node_entry.cost,cn)

            visited.add(cn)


    for i,v in lookup.items():
        if v.cost < INF:
            print (i,v)
    return lookup

def build_graph( memory, corrupted):

    graph =dict()

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for m in memory:
        if m in corrupted:
            print(m,"corrupted")
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

            

Cell = namedtuple("Cell", ["pos","g","h"])


def dist_manhattan(a,b):
    return abs(b[0] - a[0]) + abs(b[1] -a[1])


def a_star(start,end, graph):
        
    de = set([Cell(start, 0 , dist_manhattan(start,end))])
    visited = set()

    while True:

    # for _ in range(1000):

        print("---------")
        f = INF 
        next_cell : Cell = Cell(None,None,None)

        for cell in de.copy():
            next_cell = cell if cell.g + cell.h < f else next_cell
            f = cell.g + cell.h if cell.g + cell.h < f else f
        de.remove(next_cell)
        visited.add(next_cell.pos)

        if next_cell.pos == end:
            print(next_cell)
            break
        else:
            edges = graph.get(next_cell.pos,[])
            for edge_node ,dist in edges.items():

                if not edge_node in visited:
                    de.add( Cell(edge_node, dist+next_cell.g , dist_manhattan(edge_node,end))  )

def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    num_bytes = 1024
    corrupted = []

    for line in lines:
        a,b = line.split(",")
        corrupted.append((int(a),int(b)))

    # max_i, max_j = 7,7
    max_i, max_j = 71,71

    buffer = [ ["." for j in range(max_j)] for i in range(max_i) ]

    memory = {(i,j) for j in range(max_j) for i in range(max_i)}

    for i in range(num_bytes):
        c = corrupted[i]
        pi,pj = c[0],c[1]
        print(pi,pj)
        buffer[pi][pj] = "#"

    g= build_graph(memory,corrupted[:num_bytes])

    for b in g.keys():
        print(b)
        buffer[b[0]][b[1]] = "+"



    print(NEW_LINE.join([ "".join(row) for row in buffer ]))

    path = a_star((0,0),(max_i-1,max_j-1),g)

    #
    # print("FFF",lookup.get((70,70)))

    # print(lookup)
    
    

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
