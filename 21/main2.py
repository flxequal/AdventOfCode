import itertools


num_pad = ["7","8","9","4","5","6","1","2","3",None,"0","A"]
num_pad_to_idx = { v:i for i,v in enumerate(num_pad)}

dir_pad = [None, "^","A","<","v",">"]
dir_pad_to_idx = { v:i for i,v in enumerate(dir_pad)}

dir_costs = {
        "A": {"^":1, ">":1, "v":2,"<":3},
        "^": {"A":1, ">":2, "v":1,"<":2},
        ">": {"^":2, "A":1, "v":1,"<":2},
        "v": {"^":1, ">":1, "A":2,"<":1},
        "<": {"^":2, ">":2, "v":1,"A":3},
        }

dir_paths = {
        "A": {"^":"<", ">":"v", "v":"v<","<":"v<<"},
        "^": {"A":">", ">":"v>", "v":"v","<":"v<"},
        ">": {"^":"^<", "A":"^", "v":"<","<":"<<"},
        "v": {"^":"^", ">":">", "A":">^","<":"<"},
        "<": {"^":">^", ">":">>", "v":">","A":">>^"},
        }

def move_possibilities(i,j):
    v=(j//3-i//3)
    h=(j%3-i%3)
    steps_h = abs(h) * ("<" if h<0 else ">")
    steps_v = abs(v) * ("^" if v<0 else "v")
    return  set([ "".join(list(i)) for i in itertools.permutations([steps_v,steps_h])])

def move_possibilities_dir_pad(a,b):
    ia = dir_pad_to_idx[a]
    ib = dir_pad_to_idx[b]
    return move_possibilities(ia,ib)

def move_possibilities_num_pad(a,b):
    ia = num_pad_to_idx[a]
    ib = num_pad_to_idx[b]
    pad = []
    for m in move_possibilities(ia,ib):
        tmp_a = ia
        valid = True
        for step in m:
            if step == "<":
                tmp_a -=1
            elif step == "^":
                tmp_a -=3
            elif step == ">":
                tmp_a +=1
            elif step == "v":
                tmp_a +=3
            else:
                pass
            if tmp_a == 9:
                valid = False
        if valid:
            pad.append(m)
    return pad



def calc_costs(code):
    start = "A"
    score = 0
    for c in code:
        if c == start :
            continue
        cost  = dir_costs[start][c]
        score+= cost
        start =c

    return score

def evolve(code):
    start="A"
    patterns = []
    for c in code:
        p = move_possibilities_dir_pad(start,c)
        patterns.append(p)
        start = c
    return patterns

def evolve2(code):
    start="A"
    patterns = ""
    for c in code:
        if c ==start :
            patterns += "A"
            continue

        p = dir_paths[start][c]
        patterns +=p+"A"
        start = c
    return patterns

def calc_paths_from_options(options):

    paths = [""]
    for opt in options:
        tmp_paths = []
        for o in list(opt):
            for p in paths:
                tmp_paths.append(p + o + "A")
        paths = tmp_paths
            
    return paths


def num_pad_steps(code):
    start="A"
    poss = []
    for c in code:
        p = move_possibilities_num_pad(start,c)
        start = c
        poss.append(p)
    return poss


cache = {}

def evovle_step(a,b,depth):

    global cache
    if a == b and a =="A":
        return 1
    if depth == 0:
        return 1
    res = cache.get((a,b,depth),None)
    if not res:
        if a == b:
            code = "A"
            return 1
        else:
            code = dir_paths[a][b]
        start="A"
        res = 0
        for c in code:
            res += evovle_step(start,c,depth-1)
            start =c

        res += evovle_step(start,"A",depth-1)
        cache[(a,b,depth)] = res
    return res

def main():


    res = 0 
    # for code in ["029A"]: #,"980A","179A","456A","379A"]:
    # for code in ["029A","980A","179A","456A","379A"]:
    for code in ["789A", "540A", "285A", "140A", "189A"]:
        paths = calc_paths_from_options(num_pad_steps(code))
        print(paths)
        score = 10e99
        #
        top_path = ""
        for path in paths:
            start="A"
            tmp_res = 0
            for c in path:
                tmp_res += evovle_step(start,c,25)
                start = c
            print(tmp_res)
            if tmp_res<=score:
               score = tmp_res
               top_path =path

        res += int(code[:-1]) * score
        print(code,score, int(code[:-1]) * score )
        print(code)

    print(res)

if __name__ == "__main__":
    main()
