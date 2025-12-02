
NEW_LINE = "\n"


def read_input(file_name):
    with open (file_name,"r") as fp:
        data = fp.read()
        return data

def is_safe_report(report):
    diffs = [ report[i+1] - report[i]   for i in range(len(report)-1) ]
    monotonic = len( {d > 0 for d in diffs}) == 1
    in_bounds = not any([ True for d in diffs if abs(d)<1 or abs(d)>3 ])
    return monotonic and in_bounds


def is_safe_report_with_tolerance(report):

    if is_safe_report(report):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe_report(new_report):
            return True

    
    return False


def main():

    data = read_input("./input.yannick")
    lines = [ line for line in data.split(NEW_LINE) if line.strip()]
    result = 0

    for i, line in enumerate(lines):
        report = [int(e) for e in line.split(" ")]
        result =  result +1 if is_safe_report_with_tolerance(report) else result
        if is_safe_report_with_tolerance(report):
            print(i,line)

    print(result)

if __name__ == "__main__":
    main()
