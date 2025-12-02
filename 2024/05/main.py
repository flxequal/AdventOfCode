

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

def is_valid_ordering(steps, rule_map):
    is_valid = True
    for i in range(len(steps)-1):
        current = steps[i]
        rest = steps[i+1:]
        must_before = rule_map.get(current,[])
        for r in rest:
            is_valid = is_valid and (r in must_before)
    return is_valid

def main():

    data = read_input(INPUT_FILE)
    rule_data,job_data = data.split(2*NEW_LINE)

    rules = [r.strip() for r in rule_data.split(NEW_LINE) if r]
    jobs = [r.strip() for r in job_data.split(NEW_LINE) if r]
    rule_map = dict() 

    for r in rules:
        a,b = r.split("|")
        must_before = rule_map.get(a,set())
        must_before.add(b)
        rule_map[a]=must_before

    result = 0

    for job in jobs:
        steps = job.split(",")
        if is_valid_ordering(steps,rule_map):
            mid = steps[len(steps)//2]
            result += int(mid)

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
