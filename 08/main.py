
import itertools

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""



def main():

    lines = read_input_as_lines(INPUT_FILE)
    antennas = dict()

    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            
            if cell != ".":
                nodes = antennas.get(cell,[])
                nodes.append((i,j))
                antennas[cell] = nodes

    imax = len(lines)
    jmax =len(lines[0])

    antinodes = set()
# <<<<<<< HEAD

    for _,nodes in antennas.items():

        for k ,_ in enumerate(nodes):
# =======
#     print(antennas)
#
#     for a,nodes in antennas.items():
#
#
#         print(a,nodes)
#         for k ,n in enumerate(nodes):
# >>>>>>> 97241bb (initial commit)
            for l in range(k+1,len(nodes)):

                n1 = nodes[k]
                n2 = nodes[l]

                di = n2[0]-n1[0]
                dj = n2[1]-n1[1]

                an1_i = n1[0] - di
                an1_j = n1[1] - dj

                an2_i = n2[0] + di
                an2_j = n2[1] + dj

# <<<<<<< HEAD
# =======
#                 print(n1,n2)
#
#                 print(an1_i,an1_j)
#                 print(an2_i,an2_j)
#
# >>>>>>> 97241bb (initial commit)
                if an1_i >=0 and an1_i < imax and an1_j >=0 and an1_j < jmax:
                   antinodes.add((an1_i,an1_j))
                if an2_i >=0 and an2_i < imax and an2_j >=0 and an2_j < jmax:
                   antinodes.add((an2_i,an2_j))


# <<<<<<< HEAD
    print(len(antinodes))

# =======
#
#     print(antinodes)
#     print(len(antinodes))
#
#
#
#
#
#     # C O D E
#
#     print(result)
#
#
#
# >>>>>>> 97241bb (initial commit)
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
