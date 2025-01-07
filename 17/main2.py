


def calc(a_in):
    a,b,c = a_in,0,0
    out = "0"
    while a>0:
        b = (a%8) & 7       
        b = b ^ 7           
        c = int(a / (2**b)) 
        a = int(a/(2**3))   
        b = b ^ c
        b = b ^ 7
        out += str(b%8)
    
    s = [ i for i,c in enumerate(out) if c != "0"]
    istart = s[0] if len(s)!=0 else 0
    return int(out[istart::])

goal = str(2417750344175530)
start = [""]

for i in range(22):
    new_start = []
    for s in start:
        for i in range(8):
            a = int(s + str(i),8)
            res = calc(a)
            if goal.endswith(str(res)):
                new_start.append(s+str(i))

    start = new_start.copy()
    for s in new_start:
        res = calc(int(s,8))
        if res == int(goal):
            print("possible program",s)


