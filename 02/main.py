

NEW_LINE = "\n"


def read_input(file_name):
    with open (file_name,"r") as fp:
        data = fp.read()
        return data


def main():

    data = read_input("./input.txt")

    lines = [ line for line in data.split(NEW_LINE) if line.strip()]

    result = 0
    for line in lines:
        report = [int(e) for e in line.split(" ")]
        diffs = [ report[i+1] - report[i]   for i in range(len(report)-1) ]
        monotonic = len( {d > 0 for d in diffs}) == 1
        in_bounds = not any([ True for d in diffs if abs(d)<1 or abs(d)>3 ])

        result = result +1 if monotonic and in_bounds else result

    print(result)





if __name__ == "__main__":
    main()
