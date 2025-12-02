

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
2333133121414131402
"""



def main():

    lines = read_input_as_lines(INPUT_FILE)

    isFile = True
    blocks = []
    id = 0

    for i , f in enumerate(lines[0]):
        if isFile:
            blocks += [id for _ in range(int(f))]
            id +=1
        else:
            blocks += ["." for _ in range(int(f))]
        isFile = not isFile

    i=0

    while True:
        if i == len(blocks):
            break

        c = blocks[i]
        if c == ".":
            f = blocks.pop()
            if f != ".":
                blocks[i]=f
            else:
                continue
        i+=1

    
    checksum = sum([i*v for i,v in enumerate(blocks)])
    print(checksum)

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
