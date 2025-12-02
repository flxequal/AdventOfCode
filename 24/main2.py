import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

y02 OR x01 -> tnw
x00 OR x03 -> fst
y03 OR y00 -> psh
y00 AND y03 -> djm
x03 OR x00 -> vdt
x04 AND y00 -> kjc
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
y01 AND x02 -> pbm
y04 OR y02 -> fgs
y03 OR x01 -> nrd
ntg XOR fgs -> mjb
vdt OR tnw -> bfw
ffh OR nrd -> bqk
tnw OR fst -> frj
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
ntg OR kjc -> kwq
psh XOR fgs -> tgd
pbm OR djm -> kpj
nrd XOR fgs -> wpb
tnw OR pbm -> gnj
bfw XOR mjb -> z00
tgd XOR rvg -> z01
gnj AND wpb -> z02
hwm AND bqk -> z03
frj XOR qhw -> z04
kwq OR kpj -> z05
bfw OR bqk -> z06
bqk OR frj -> z07
bqk OR frj -> z08
qhw XOR tgd -> z09
bfw AND frj -> z10
gnj AND tgd -> z11
tgd XOR rvg -> z12
"""


Operation = namedtuple("Operation",["input", "operation","rv"])

def read_combined_input(data):
    start, logic = data.split(NEW_LINE + NEW_LINE,2)

    wires = dict()
    operations = []

    for s in [l for l in start.split(NEW_LINE) if l.strip() ]:
        # print(s)
        wire, num = s.split(":")
        wires[wire]  = int(num.strip())

    for op in [ o for o in logic.split(NEW_LINE) if o.strip() ]:
        a, bool_op, b, _, w = op.split(" ")
        operations.append(tuple([ (a,b), bool_op, w]))
    # print(operations)
    return wires,operations


def main():

    # --- read data
    data = read_input(INPUT_FILE)
    # lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    data = SAMPLE
    lines = input_to_lines(SAMPLE)

    wires, operations = read_combined_input(data)

    # while len(operations):
    #     tmp_ops = operations
    #     visited = []
    #     tmp_dict = dict()
    #     for i,op in enumerate(tmp_ops):
    #         a,b = op[0]
    #
    #         if a in wires and b in wires:
    #             visited.append(operations.pop(i))
    #             va = wires[a]
    #             vb = wires[b]
    #             operand = op[1]
    #             lv = op[2]
    #             res = None
    #             if operand == "AND":
    #                 res = va & vb
    #             elif operand == "OR":
    #                 res = va | vb
    #             elif operand == "XOR":
    #                 res = va ^ vb
    #             tmp_dict[lv]=res
    #     wires.update(tmp_dict)
    #     print([ v[0] for v in visited])
    
    graph = dict()
    for op in operations:
        foo = op[2]
        graph[foo] = (op[0], op[1])

    def get_parents(child):

        if not child in graph:
            return 

        parent,op = graph.get(child,(None,None))

        for p in parent:
            get_parents(p)





    keys = [ k  for k,v in wires.items() if k.startswith("z")]
    keys.sort()

    foo = sum([wires[k]<<i for i,k in enumerate(keys)])

    print(foo)




    

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
