import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

# SAMPLE="""
# #################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################
# """

HORZ = "horz"
VERT = "vert"

INF = 10e16

Node = namedtuple("Node",["pos"])
NodeWithDir = namedtuple("Node",["pos","dir"])
Edge = namedtuple("Edge",["pair","len"])


def edge_direction (edge):
    n1 = edge.pair[0]
    n2 = edge.pair[1]

    if n1.pos[0] - n2.pos[0] == 0 :
        return HORZ
    return VERT

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

def calc_intersections(start,end,paths):

    nodes = []
    s = Node(start)
    e = Node(end)

    nodes.append(s)
    nodes.append(e)

    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for p in paths:
        possible_dirs = []
        for d in directions:
            ni = p[0] + d[0]
            nj = p[1] + d[1]
            if (ni,nj) in paths:
                possible_dirs.append((d[0],d[1]))
        if len(possible_dirs)>2:
            nodes.append(Node(p))
        elif len(possible_dirs) ==2 :
            a = possible_dirs[0][0] + possible_dirs[1][0]
            b = possible_dirs[0][1] + possible_dirs[1][1]
            # print(possible_dirs,a+b>0)
            if abs(a)+abs(b)>0:
                nodes.append(Node(p))

    return nodes




def calc_edges (intersections,walls):

    directions  = [(1,0),(0,1),(-1,0),(0,-1)]
    edges = []
    for inter in intersections:
        for d in directions:
            i = 1
            while True:

                pi = inter.pos[0] + d[0] * i
                pj = inter.pos[1] + d[1] * i

                if (pi,pj) in walls:
                    break

                if Node((pi,pj)) in intersections:
                    orientaion = "horz"
                    if d[0]!=0:
                        orientaion = "vert"
                    e1 = Edge((inter,Node((pi,pj))),i)
                    e2 = Edge( (Node((pi,pj)),inter ),i)
                    if not e1 in edges and not e2 in edges:
                        edges.append(e1)
                    break
                i+=1
    return edges
                    

def dijkstra (graph,start,end):

    visited = set()
    Entry = namedtuple("Entry",["node","cost","pre"])
    lookup = dict()
    lookup_with_paths = dict()

    best_paths = []

    for k,_ in graph.items():
        if k != start:
            lookup[k]=Entry(k,INF,None)
        else:
            lookup[k]=Entry(k,0,k)

    current_nodes = [start]

    while len(visited) != len(graph):
    # for i in range(100):

        tmp_cost = INF
        new_node = None
        current_nodes = []
        for k,v in lookup.items():
            if not k in visited:
                if tmp_cost > v.cost:
                    tmp_cost = v.cost
                    new_node = k

        print("choose", new_node)

        if new_node:
            current_nodes.append(new_node)

        for cn in current_nodes:
            edges = graph.get(cn)
            for n, dist in edges.items():
                if n in visited:
                    continue
                current_node_entry = lookup[cn]
                foo = lookup[n]
                score = dist + current_node_entry.cost
                if foo.cost > dist+current_node_entry.cost:
                    # print("UPDATE ENTRY",n, Entry(n,dist,cn))
                    if n.pos == end:
                        best_paths.append(Entry(n,dist+current_node_entry.cost,cn))

                    lookup[n]=Entry(n,dist+current_node_entry.cost,cn)

                traces = lookup_with_paths.get(n,set())
                if traces:
                    t = list(traces)[0]
                    if t.cost > score:
                        traces = {Entry(n,dist+current_node_entry.cost,cn)}
                    if t.cost == score:
                        traces.add(Entry(n,dist+current_node_entry.cost,cn))
                else:
                    traces = {Entry(n,dist+current_node_entry.cost,cn)}
                lookup_with_paths[n]=traces



            visited.add(cn)


    for i,v in lookup.items():
        if v.cost < INF:
            print (i,v)

    return lookup, lookup_with_paths

        





def main():


    # lines = input_to_lines(SAMPLE)


    data = read_input(INPUT_FILE)
    lines = input_to_lines(data)
    # data = SAMPLE

    # lines = input_to_lines(SAMPLE)
    grid = [[c for c in line] for line in lines]
    

    walls,paths, reindeer, end = read_maze(data)
    intersects =  calc_intersections(reindeer,end,paths)
    edges = calc_edges(intersects,walls)

    graph = dict()

    for e in edges:
        n1 = e.pair[0]
        n2 = e.pair[1]

        n1wd = NodeWithDir(n1, edge_direction(e))
        n2wd = NodeWithDir(n2, edge_direction(e))
        other_dir = VERT if edge_direction(e) == HORZ else HORZ
        n1wd_rotated = NodeWithDir(n1,other_dir)
        n2wd_rotated = NodeWithDir(n2,other_dir)

        neighbours_n1 = graph.get(n1wd,dict())
        neighbours_n2 = graph.get(n2wd,dict())
        neighbours_n1_rotated = graph.get(n1wd_rotated,dict())
        neighbours_n2_rotated = graph.get(n2wd_rotated,dict())


        neighbours_n1[n1wd_rotated]=1000
        neighbours_n1_rotated[n1wd]=1000
        neighbours_n1[n2wd] = e.len

        neighbours_n2[n2wd_rotated]=1000
        neighbours_n2_rotated[n2wd]=1000
        neighbours_n2[n1wd] = e.len

        graph[n1wd] = neighbours_n1
        graph[n2wd] = neighbours_n2
        graph[n1wd_rotated] = neighbours_n1_rotated
        graph[n2wd_rotated] = neighbours_n2_rotated

    for k,v in graph.items():
        print(k,v)

    lookup, best_paths = dijkstra(graph,NodeWithDir(Node(reindeer),HORZ),Node(end))

    h = lookup.get(NodeWithDir(Node(end),HORZ))
    v = lookup.get(NodeWithDir(Node(end),VERT))

    best_end_node = h if h.cost< v.cost else v
    
    
    best_pre = best_paths.get(best_end_node.node)

    print(best_pre)

    edges = all_edges(best_pre,best_paths,NodeWithDir(Node(reindeer),HORZ))

    print(edges)

    fields_visites = set()
    for e in edges:
        # print(e)

        
        n1,n2 = list(e.pair)
        if n1.pos == n2.pos:
            fields_visites.add(n1.pos)
            continue

        print(e, edge_direction(e))

        fields_visites.add(n1.pos)
        fields_visites.add(n2.pos)

        if edge_direction(e) == HORZ:
            step = 1 if n1.pos[1] - n2.pos[1] <0 else -1
            print(n1.pos[1], n2.pos[1],step)
            for i in range(n1.pos[1],n2.pos[1],step):
                print("FOO", (n1.pos[0],i))
                fields_visites.add((n1.pos[0],i))
        else:
            step = 1 if n1.pos[0] - n2.pos[0] <0 else -1
            for i in range(n1.pos[0],n2.pos[0],step):
                print("FOO", (i,n1.pos[1]))
                fields_visites.add((i,n1.pos[1]))

    for f in fields_visites:
        grid[f[0]][f[1]] = "o"


    buffer  =  NEW_LINE.join([ "".join(row) for row in grid ])

    print(buffer)
    print(len(fields_visites))

def all_edges (start,best_paths,end):
    new_pre ,old_pre = set(), set()
    for s in list(start):
        old_pre.add(s)
    edges = set()

    while True:
        for p in old_pre:
            a = best_paths.get(p.pre)
            if not a :
                continue
            for aa in a:
                edges.add(Edge((p.node.pos,aa.node.pos),-1))
                new_pre.add(aa)
        if len(new_pre) == 0:
            break

        old_pre = new_pre.copy()
        new_pre = set()

    return edges
        







    





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
