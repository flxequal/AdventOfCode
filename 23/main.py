import re
from collections import namedtuple

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

    print(graph)

    cycles = set()

    for node, edges in graph.items():
        for e in edges:
            edges2 = graph.get(e,[])
            for e2 in  edges2:
                if node in graph.get(e2,[]):
                    a=[node,e,e2]
                    a.sort()
                    cycles.add(tuple(a))
            # third_node = graph.get(e,[])
            # if node in third_node:
                # cycles.add({node,e ,})
    res = 0

    for c in cycles:
        print(c)

    print(len(cycles))

    for cycle in cycles :
        t = "".join(c[0] for c in cycle)
        if "t" in t:
            res +=1

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
