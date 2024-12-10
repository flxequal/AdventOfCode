import time

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

    t0 = time.time()

    for i , f in enumerate(lines[0]):
        if isFile:
            blocks += [id for _ in range(int(f))]
            id +=1
        else:
            blocks += ["." for _ in range(int(f))]
        isFile = not isFile


    start = 0
    end = 0
    last_block = ""
    free_sections = []
    for i,c in enumerate(blocks):
        if c == "." and last_block != ".":
            start = i 
        elif c !="." and last_block == ".":
            end = i
            free_sections.append((start,end))
        last_block = c

    back_start = len(blocks)-1
    while back_start>0:

        tmp_block = []

        while True:
            c = blocks[back_start]
            if len(tmp_block) == 0:
                tmp_block.append(c)
                back_start -= 1
            elif tmp_block[-1] == c:
                tmp_block.append(c)
                back_start -= 1
            else:
                break

        # skip if block is empty
        l = len(tmp_block)
        if set(tmp_block).pop() ==".":
            continue

        # write file data at next free position

        for i, fs in enumerate(free_sections):
            fs_start = fs[0]
            fs_end = fs[1]

            if fs_start > back_start:
                break

            fs_len = fs_end - fs_start

            if fs_len >= l:
                for j,b in enumerate(tmp_block):
                    blocks[fs_start +j] = b
                    blocks[1+back_start+j] = "."

                if fs_len ==l:
                    free_sections.pop(i)
                else:
                    free_sections[i] = (fs_start +l, fs_end)
                break
        
    checksum = sum([i*v for i,v in enumerate(blocks) if v != "."])

    print("time: ", time.time()-t0)

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
