import re
from collections import namedtuple

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

SAMPLE="""
Register A: 0
Register B: 0
Register C: 9

Program: 2,6
"""

SAMPLE="""
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
"""

REG_A = 0
REG_B = 0
REG_C = 0

PROGRAM = []

INSTRUCTION_POINTER = 0
STDOUT = []

def adv():
    global REG_A , INSTRUCTION_POINTER
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    operand = read_combo_operand(operand)
    print("devide a with 2^op to A , op", PROGRAM[INSTRUCTION_POINTER +1])
    # print("adv", REG_A, operand**2)
    REG_A = int(REG_A / (2**operand))
    INSTRUCTION_POINTER +=2

def bxl():
    global REG_B , INSTRUCTION_POINTER
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    print("xor b with op, op", operand)
    REG_B = REG_B ^ operand
    INSTRUCTION_POINTER +=2

def bst():
    global REG_B , INSTRUCTION_POINTER
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    operand = read_combo_operand(operand)
    print("op % 8 3bit to B, op", PROGRAM[INSTRUCTION_POINTER +1], "combo" , operand)
    REG_B = (operand % 8) & 7
    INSTRUCTION_POINTER +=2

def jnz():
    global REG_A, REG_B , INSTRUCTION_POINTER
    if REG_A == 0:
        INSTRUCTION_POINTER += 2
        return
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    print("JUMP to 0")
    INSTRUCTION_POINTER = operand

def bxc():
    global REG_B,INSTRUCTION_POINTER, REG_C
    print("xor B and C to B")
    REG_B = REG_C ^ REG_B
    INSTRUCTION_POINTER += 2

def out():
    global REG_B,INSTRUCTION_POINTER, STDOUT
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    print("out", operand)
    operand = read_combo_operand(operand)
    print(operand,operand %8)
    STDOUT.append(operand%8)
    INSTRUCTION_POINTER += 2

def bdv():
    global REG_B, REG_A , INSTRUCTION_POINTER
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    operand = read_combo_operand(operand)
    print(f"DEVIDE A / 2^op to B op {PROGRAM[INSTRUCTION_POINTER + 1]}, combo {operand}")
    REG_B = int(REG_A / (2**operand))
    INSTRUCTION_POINTER +=2

def cdv():
    global REG_C, REG_A , INSTRUCTION_POINTER
    operand = PROGRAM[  INSTRUCTION_POINTER + 1 ]
    operand = read_combo_operand(operand)
    print(f"DEVIDE A / 2^op to C op {PROGRAM[INSTRUCTION_POINTER + 1]}, combo {operand}")
    REG_C = int(REG_A / (2**operand))
    INSTRUCTION_POINTER +=2


def read_combo_operand(operand:int)-> int:
    op = operand
    if operand<4:
        op = operand
    elif operand == 4:
        print("load reg A", REG_A)
        op = REG_A
    elif operand == 5:
        op = REG_B
    elif operand == 6:
        op = REG_C
    elif operand ==7 :
        op = operand
    return op

def main():

    global PROGRAM, INSTRUCTION_POINTER, REG_A, REG_B, REG_C

    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 


    data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    for line in lines:
        if  "Register A:" in line:
            REG_A = int(line.split(":")[1].strip())
        if  "Register B:" in line:
            REG_B = int(line.split(":")[1].strip())
        if  "Register C:" in line:
            REG_C = int(line.split(":")[1].strip())
        if  "Program:" in line:
            PROGRAM = [ int(c) for c in line.split(":")[1].strip().split(",")]

    halt = False


    while not halt:
    # for _ in range(10):
        # print(f"A: {REG_A} \nB: {REG_B} \nC: {REG_C} \nIP: {INSTRUCTION_POINTER}")
        # print("  "* INSTRUCTION_POINTER + "v")
        # print(" ".join(str(c) for c in PROGRAM))
        # input("press enter")

        if INSTRUCTION_POINTER >= len(PROGRAM):
            break
        opcode = PROGRAM[INSTRUCTION_POINTER]
        if opcode == 0:
            adv()
        elif opcode ==1:
            bxl()
        elif opcode ==2:
            bst()
        elif opcode ==3:
            jnz()
        elif opcode ==4:
            bxc()
        elif opcode ==5:
            out()
        elif opcode ==6:
            bdv()
        elif opcode ==7:
            cdv()

        if INSTRUCTION_POINTER > len(PROGRAM):
            halt = True

        if halt:
            return


    print(REG_A, REG_B,REG_C,PROGRAM)

    print(STDOUT)

    print(",".join([str(i) for i in STDOUT]))




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
