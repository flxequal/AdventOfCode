

NEW_LINE = "\n"
INPUT_FILE = "input.txt"

swap_with_prev = lambda arr, i : arr[:i-1] + [arr[i]] + [arr[i-1]] + arr[i+1:]


def main():

    result = 0

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

    for job in jobs:
        steps = job.split(",")
        is_valid = is_valid_ordering(steps,rule_map)
                
        if not is_valid :

            tmp_is_correct = False
            while not tmp_is_correct:
                for i, step in enumerate(steps):
                    before = set(steps[:i])
                    must_be_after = rule_map.get(step,set([]))
                    inter = must_be_after.intersection(before)
                    if len(inter)>0:
                        steps = swap_with_prev(steps,i)
                        break

                tmp_is_correct = is_valid_ordering(steps, rule_map)
            result += int(steps[len(steps)//2],10)


    print("RESULT",result)



# --- common helper functions ---
def is_valid_ordering(steps, rule_map):
    is_valid = True
    for i in range(len(steps)-1):
        current = steps[i]
        rest = steps[i+1:]
        must_before = rule_map.get(current,[])

        for r in rest:
            is_valid = is_valid and (r in must_before)

    return is_valid

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
