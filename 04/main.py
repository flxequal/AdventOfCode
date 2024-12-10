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
    # --- read data
    # data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)


    M= [ [c for c in l] for l in lines]

    i_max = len(M[0])
    j_max = len(M)

    t2b = [  M[j][i]  for i in range(i_max) for j in range(j_max)]
    l2r = [  M[i][j]  for i in range(i_max) for j in range(j_max)]

    l2r = " ".join([ "".join([ M[i][j] for j in range(j_max)  ]) for i in range(i_max)])
    t2b = " ".join([ "".join([ M[j][i] for j in range(j_max)  ]) for i in range(i_max)])
    diag_tr = ""
    diag_tr_r = ""
    diag_tl= ""
    diag_tl_r = ""

    i_range = [0 for _ in range(i_max)] + [ i for i in range(1,i_max) ]
    j_range = [i for i in range(j_max)][::-1] + [ 0 for _ in range(1,i_max) ]

    for i,j in zip(i_range, j_range):

        while (i < i_max and j< j_max):
            c = M[i][j]
            diag_tr += c
            i+=1
            j+=1
        diag_tr += " "


    i_range = [0 for _ in range(i_max)] + [ i for i in range(1,i_max) ]
    j_range = [i for i in range(j_max)] + [ j_max -1 for _ in range(1,i_max) ]

    for i,j in zip(i_range, j_range):

        while (i < i_max and j>=0):
            c = M[i][j]
            diag_tl += c
            i+=1
            j-=1
        diag_tl += " "


    diag_tr_r = diag_tr[::-1]
    diag_tl_r = diag_tl[::-1]
    r2l = l2r[::-1]
    b2t = t2b[::-1]

    result = 0

    result += len(re.findall("XMAS",diag_tl_r))
    result += len(re.findall("XMAS",diag_tl))
    result += len(re.findall("XMAS",diag_tr_r))
    result += len(re.findall("XMAS",diag_tr))

    result += len(re.findall("XMAS", r2l))
    result += len(re.findall("XMAS", l2r))
    result += len(re.findall("XMAS", t2b))
    result += len(re.findall("XMAS", b2t))

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
