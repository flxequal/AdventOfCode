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

SAMPLE="""
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

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
                    

def dijkstra (graph,start):

    visited = set()
    Entry = namedtuple("Entry",["node","cost","pre"])
    lookup = dict()

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
                if foo.cost > dist+current_node_entry.cost:
                    # print("UPDATE ENTRY",n, Entry(n,dist,cn))
                    lookup[n]=Entry(n,dist+current_node_entry.cost,cn)

            visited.add(cn)


    for i,v in lookup.items():
        if v.cost < INF:
            print (i,v)
    return lookup

        





def main():


    # lines = input_to_lines(SAMPLE)

    data = read_input(INPUT_FILE)
    # data = SAMPLE
    

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



        # neighbours_n2[n1wd_rotated]=1000
        # neighbours_n1[n2wd] = e.len

        
    

        # for d in [HORZ,VERT]:
        #     nwd = NodeWithDir(n1,d)
        #
        #     other_nodes = graph.get(nwd,dict())
        #     other_dir = VERT if d == HORZ else HORZ
        #     other_nodes[NodeWithDir(n1,other_dir)] = 1000
        #
        #     edge_dir = edge_direction(e)
        #     other_nodes[NodeWithDir(n2,edge_dir)] = e.len
        #
        #
        #     onode = graph.get(n2,dict())
        #     onode[NodeWithDir(n1, edge_direction)] = e.len
        #     other_dir = VERT if d == HORZ else HORZ
        #     onode[NodeWithDir]





            # for d1 in [HORZ,VERT]:
            #     nwd2 = NodeWithDir(n2,d1)
            #     score = INF
            #     if d1 == d:
            #         score = e.len
            #     else :
            #         score = e.len + 1000
            #     other_nodes[nwd2] = score
            #     foo = graph.get(nwd2,dict())
            #     foo[nwd] = score
            #     graph[nwd2]=foo

    # return graph


    for k,v in graph.items():
        print(k,v)

    lookup = dijkstra(graph,NodeWithDir(Node(reindeer),HORZ))

    h = lookup.get(NodeWithDir(Node(end),HORZ))
    v = lookup.get(NodeWithDir(Node(end),VERT))

    print(h,v)

    # print(edges)

    # grid = [[ c for c in line ]for line in lines ]
    #
    # print(grid)

    # for inter in intersects:
    #     pi = inter.pos[0]
    #     pj = inter.pos[1]
    #     grid[pi][pj] = "x"

    # print(grid)

    # foo = NEW_LINE.join([ "".join(row) for row in grid ])

    # print(foo)


    # print(set(intersects))

    # score = find_path(Node(reindeer),Node(end),intersects, edges)
    # score = find_path_recursive(Node(reindeer),Node(end),"horz",set(edges))
    





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
