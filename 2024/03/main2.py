

import re

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def main():

    data = read_input(INPUT_FILE)
    matches = re.findall("(mul\\(\\d{1,3},\\d{1,3}\\)|do(n't)?)",data)

    result = 0
    mul_enabled = True

    for m in matches:
        if m[0] == "do":
            mul_enabled = True
            continue
        elif m[0] == "don't":
            mul_enabled = False
            continue

        if mul_enabled:
            s = m[0].strip("mul(").strip(")")
            a,b = s.split(",",1)
            result += int(a,10)*int(b,10)

    print(result)


def read_input(file_name):
    with open (file_name,"r") as fp:
        data = fp.read()
        return data

if __name__ == "__main__":
    main()
