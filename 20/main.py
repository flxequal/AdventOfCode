import re
from collections import namedtuple

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
NodeWithDir = namedtuple("Node",["pos","dir"])
Edge = namedtuple("Edge",["pair","len"])
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
                    # orientaion = "horz"
                    # if d[0]!=0:
                        # orientaion = "vert"
                    e1 = Edge((inter,Node((pi,pj))),i)
                    e2 = Edge( (Node((pi,pj)),inter ),i)
                    if not e1 in edges and not e2 in edges:
                        edges.append(e1)
                    break
                i+=1
    return edges

def dijkstra (graph,start):

    visited = set()
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

        # print("choose", new_node)

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


    # for i,v in lookup.items():
    #     if v.cost < INF:
            # print (i,v)
    return lookup


CheatWall =  namedtuple("CheatWall",["n1","n2"])

def calc_cheat_walls(walls,max_i,max_j)-> set[CheatWall]:

    directions  = [(1,0),(0,1),(-1,0),(0,-1)]
    cheat_walls = set()

    for w in walls:

        h1 = (w[0] + 0 , w[1] + 1)
        h2 = (w[0] + 0 , w[1] - 1)

        if not h1 in walls and not h2 in walls:
            in_bound1 = 0< h1[0] and h1[0] < max_i
            in_bound2 = 0< h1[1] and h1[1] < max_j

            in_bound3 = 0< h2[0] and h2[0] < max_i
            in_bound4 = 0< h2[1] and h2[1] < max_j

            if not False in {in_bound1,in_bound2,in_bound3,in_bound4}:
                cheat_walls.add(CheatWall(Node(h1),Node(h2)))

        h1 = (w[0] + 1 , w[1] + 0)
        h2 = (w[0] - 1 , w[1] + 0)

        if not h1 in walls and not h2 in walls:
            in_bound1 = 0< h1[0] and h1[0] < max_i
            in_bound2 = 0< h1[1] and h1[1] < max_j

            in_bound3 = 0< h2[0] and h2[0] < max_i
            in_bound4 = 0< h2[1] and h2[1] < max_j

            if not False in {in_bound1,in_bound2,in_bound3,in_bound4}:
                cheat_walls.add(CheatWall(Node(h1),Node(h2)))

    return cheat_walls
        # for d in directions:




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
                

                

        







# def calc_walls_of_edge(n1,n2):
#     directions  = [(1,0),(0,1),(-1,0),(0,-1)]
#     d0 = n2[0] - n1[0] 
#     d1 = n2[1] - n1[1]
#
#     bla = lambda x : 1 if x != 0 else 0
#     sign = lambda x : -1 if x<0 else 1
#     d0 = sign(d0)  *bla(d0)
#     d1 = sign(d1) * bla(d1)
#
#     current = n1
#     walls = []
#     i=1
#     while current != n2:
#         for d in [1,-1]:
#             x=current[0] + d * d1
#             y=current[1] + d * d0
#             walls.append((x,y))
#
#         current = (current[0] + d0 , current[1] + d1)
#         # print(current,d0,d1)
#
#     return walls


# def calc_path(path,)



def main():

    # --- read data
    data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    walls, race_track,start, end = read_maze(data)


    # inters = calc_intersections(start,end,race_track)
    # edges = calc_edges(inters,walls)
    max_i, max_j =len(lines), len(lines[0])
    cheat_walls = calc_cheat_walls(walls,max_i,max_j)

    # print(cheat_walls)
    path = calc_path(race_track,Node(start),Node(end))

    # print(path)

    cheats = dict()

    buffer = [ ["." for j in range(max_j)] for i in range(max_i) ]
    for w in walls:
        i,j = w[0],w[1]
        buffer[i][j]="#"

    for cw in cheat_walls:

        # if cw.n2 == Node((7,8)):
        node1 = path.get(cw.n1)
        node2 = path.get(cw.n2)

        print(node1,node2)

        pp = cw.n1.pos
        buffer[pp[0]][pp[1]] = "c"
        pp = cw.n2.pos
        buffer[pp[0]][pp[1]] = "c"

        print(cw,node2,node1)
        max_cost = node2.cost if node2.cost > node1.cost else node1.cost
        min_cost = node2.cost if node2.cost < node1.cost else node1.cost

        reduced = max_cost  -  min_cost -2
        print(reduced)

        pico = cheats.get(reduced,0)
        cheats[reduced] =  pico +1

    print(cheats)

    res = 0
    for p,n in cheats.items():
        if p>=100:
            res +=n

    print(res)


    

    # print(race_track)
    # print(inters)
    # print(edges)

    

    # graph = dict()
    #
    # for e in edges:
    #     n1 = e.pair[0]
    #     n2 = e.pair[1]
    #
    #     edges1 = graph.get(n1,dict())
    #     edges1[n2] = e.len
    #     graph[n1] = edges1
    #
    #     edges2 = graph.get(n2,dict())
    #     edges2[n1] = e.len
    #     graph[n2] =edges2
    #
    # # print(graph)
    #
    #
    # lookup = dijkstra(graph,Node(start))
    #
    #
    #
    # print(lookup.get(Node(end)))
    #
    #
    # max_cost = lookup.get(Node(end)).cost
    #
    # path = []
    #
    # n = Node(end)
    #
    # while n != Node(start):
    # # for i in range(100):
    #     entry = lookup.get(n)
    #     path.append(n)
    #     n = entry.pre
    #     # print(entry.pre,n)
    # path.append(n)
    #
    # print(path)
    #
    #
    # for i in range(len(path)-3):
    #     e1 = path[i:i+2][0]
    #     e2 = path[i:i+2][1]
    #
    #
    #
    # for inter in inters:
    #
    #     i,j = inter.pos[0],inter.pos[1]
    #     buffer[i][j]="+"
    #
    #
    #
    # for cs in calc_cheat_walls(walls,max_i,max_j):
    #     buffer[cs[0]][cs[1]] = "c"
    #
    # cheat_walls = calc_cheat_walls(walls,max_i,max_j)
    #
    #
    # cheats = dict()
    #
    # for cheat_wall in cheat_walls:
    #
    #     print(cheat_wall)
    #     buffer[cheat_wall[0]][cheat_wall[1]]="X"
    #
    #     new_walls = walls - {cheat_wall}
    #     new_race_track = race_track | {cheat_wall}
    #     new_inters = calc_intersections(start,end,new_race_track)
    #     new_edges = calc_edges(new_inters,new_walls)
    #
    #     new_graph = dict()
    #
    #     for e in new_edges:
    #         n1 = e.pair[0]
    #         n2 = e.pair[1]
    #
    #         edges1 = new_graph.get(n1,dict())
    #         edges1[n2] = e.len
    #         new_graph[n1] = edges1
    #
    #         edges2 = new_graph.get(n2,dict())
    #         edges2[n1] = e.len
    #         new_graph[n2] =edges2
    #
    #     lookup = dijkstra(new_graph,Node(start))
    #
    #     c = max_cost-lookup.get(Node(end)).cost
    #     n = cheats.get(c,0)
    #     cheats[c] = n+1
    #
    # print(cheats)

    print(NEW_LINE.join([ "".join(row) for row in buffer ]))

    # walls, race_track,start, end = read_maze(data)
    # inters = calc_intersections(start,end,race_track)
    # edges = calc_edges(inters,walls)

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
