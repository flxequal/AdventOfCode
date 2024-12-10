

import re

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""xmul(2,4)
%&mul[3,7]!@
^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

def main():

    # --- read data
    data = read_input(INPUT_FILE)
    # lines = read_input_as_lines(INPUT_FILE)

    # --- sample data 
    # data = SAMPLE
    # lines = input_to_lines(SAMPLE)

    matches = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)",data)

    result = 0

    for m in matches:
        s = m.strip("mul(").strip(")")
        a,b = s.split(",",1)

        result += int(a,10)*int(b,10)

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
