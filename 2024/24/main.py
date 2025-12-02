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

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
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
    # data = SAMPLE
    lines = input_to_lines(SAMPLE)

    wires, operations = read_combined_input(data)

    while len(operations):
        tmp_ops = operations
        for i,op in enumerate(tmp_ops):
            a,b = op[0]
            if a in wires and b in wires:
                operations.pop(i)
                va = wires[a]
                vb = wires[b]
                operand = op[1]
                lv = op[2]
                res = None
                if operand == "AND":
                    res = va & vb
                elif operand == "OR":
                    res = va | vb
                elif operand == "XOR":
                    res = va ^ vb
                wires[lv]=res



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
