import re

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def main():

    result = 0
    lines = read_input_as_lines(INPUT_FILE)

    M= [ [c for c in l] for l in lines]

    i_max = len(M[0])
    j_max = len(M)

    for i in range(1,i_max -1):
        for j in range(1,j_max-1):
            c = M[i][j]
            if c =="A":
                ne = M[i+1][j+1]
                nw = M[i+1][j-1]
                se = M[i-1][j+1]
                sw = M[i-1][j-1]
                d1 = {ne,sw} == {"S","M"}
                d2 = {nw,se} == {"S","M"}
                if d1 and d2:
                    result += 1

    print(result)

# --- common helper functions ---

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
