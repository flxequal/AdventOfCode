
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



def calc_antinodes(n1,n2,imax,jmax):
    antinodes = set()
    di = n2[0]-n1[0]
    dj = n2[1]-n1[1]

    t=0
    while True:
        ani = n1[0] + di * t
        anj =n1[1] + dj * t
        if ani >=0 and ani < imax and anj >=0 and anj < jmax:
           antinodes.add((ani,anj))
           t+=1
        else:
           break

    t=1
    while True:
        ani = n1[0] - di*t
        anj =n1[1] - dj*t
        if ani >=0 and ani < imax and anj >=0 and anj < jmax:
           antinodes.add((ani,anj))
           t+=1
        else:
           break

    return antinodes


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

    for a,nodes in antennas.items():
        for k ,n in enumerate(nodes):
            for l in range(k+1,len(nodes)):
                n1 = nodes[k]
                n2 = nodes[l]
                ans = calc_antinodes(n1,n2,imax,jmax)
                antinodes.update(ans)
            
    print(len(antinodes))


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
