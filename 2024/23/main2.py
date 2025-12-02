import re
from collections import namedtuple

import math

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""



def main():

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    graph : dict[str,list[str]] = dict()

    for line in lines:
       a,b = line.split("-",2)
       edges = graph.get(a,[])
       edges.append(b)
       graph[a] = edges
       edges = graph.get(b,[])
       edges.append(a)
       graph[b] = edges


    histo = dict()

    for g,e in graph.items():
        for gg,ee in graph.items():
            if g == gg:
                continue
            s = {g}.union(set(e))
            ss = {gg}.union(set(ee))
            iss = ss.intersection(s)
            if len(iss) > 0 :
                tmp = list(iss)
                tmp.sort()
                tiss = tuple(tmp)
                count = histo.get(tiss,0)
                count +=1
                histo[tiss]=count

    count = 0 

    hihisto = dict()

    for h,c in histo.items():
        foo = hihisto.get(c,[])
        foo.append(h)
        hihisto[c] = foo

    sub_graph = hihisto.get( max(hihisto.keys()))[0]

    print(",".join(sub_graph))


    #
    # cache = dict()
    #
    # def get_fully_connected (sub_graph_nodes, graph):
    #
    #
    #     aa = list(sub_graph_nodes)
    #     aa.sort()
    #     taa = tuple(aa)
    #
    #     if taa in cache:
    #         return cache.get(taa), sub_graph_nodes
    #
    #
    #     max_len = len(sub_graph_nodes)
    #     max_subgraph = None
    #
    #     for n in sub_graph_nodes:
    #         next_neigh = graph[n]
    #         possible_new = set(next_neigh)-sub_graph_nodes
    #
    #         cand = []
    #         for pn in possible_new:
    #             next_next_neigh = set(graph[pn])
    #             if len(sub_graph_nodes) == len(next_next_neigh.intersection(sub_graph_nodes)):
    #                 # print("add",pn)
    #                 cand.append(pn)
    #         # print(cand)
    #
    #
    #         for c in cand:
    #             l,mm = get_fully_connected(sub_graph_nodes.union({c}), graph)
    #             # print(l)
    #             if l>max_len:
    #                 max_len = l
    #                 max_subgraph = sub_graph_nodes.union({c})
    #
    #     cache[taa] = max_len
    #     return (max_len,max_subgraph)


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
