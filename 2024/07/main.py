
import itertools

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

SAMPLE="""
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


operators = ("MUL","PLUS")

def matches_expected (nums, expected):

    num_operators = len(nums)-1
    variations = 2**num_operators
    start = 0

    for _ in range(variations):

        val = nums[0]
        ops =[ start>>i & 1 for i in range(len(nums)-1)]

        for i, op in enumerate(ops):
            if op == 0:
                val += nums[i+1]
            elif op == 1:
                val *= nums[i+1]
        if val == expected:
            return True 
        
        start += 1 
    return False

def main():

    result = 0

    data = read_input(INPUT_FILE)
    lines = read_input_as_lines(INPUT_FILE)

    for line in lines:
        expected, vals = line.split(":",2)
        nums = [int(n,10) for n in vals .strip().split(" ")]
        if matches_expected(nums, int(expected)):
            print(expected, nums)
            result += int(expected)

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
