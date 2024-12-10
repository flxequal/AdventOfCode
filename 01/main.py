


def read_input(file_name):
    with open (file_name,"r") as fp:
        data = fp.read()
        return data


def main():

    data = read_input("./input.txt")

    list_a , list_b = [] , []
    
    for line in data.split("\n"):
        vals  = line.split(" ",1)
        if len(vals) ==2 :
            a = vals[0]
            b = vals[1]
            list_a.append(int(a.strip()))
            list_b.append(int(b.strip()))

    sim_score = dict()

    for v in list_b :
        val = sim_score.get(v,0)
        sim_score[v]=val+1
    
    result = sum([ v * sim_score.get(v,0) for v in list_a ])

    print(result)


if __name__ == "__main__":
    main()
