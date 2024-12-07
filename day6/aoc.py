m = []

with open("./input.txt", "r") as f:
    lines = f.readlines()
    m = [list(line.strip()) for line in lines]

def part1(m):
    out = False
    while not out:
        for rn in range(len(m)):
            for cn in range(len(m[rn])):
                if m[rn][cn] == "^":
                    if rn == 0:
                        m[rn][cn] = "X"
                        out = True
                    elif m[rn - 1][cn] == "#":
                        m[rn][cn] = ">"
                    else: 
                        m[rn - 1][cn] = "^"
                        m[rn][cn] = "X" 
                    
                elif m[rn][cn] == "v":
                    if rn == len(m) - 1:
                        m[rn][cn] = "X"
                        out = True
                    elif m[rn + 1][cn] == "#":
                        m[rn][cn] = "<"
                    else:
                        m[rn + 1][cn] = "v"
                        m[rn][cn] = "X" 
                    
                elif m[rn][cn] == "<":
                    if cn == 0:
                        m[rn][cn] = "X"
                        out = True
                    elif m[rn][cn - 1] == "#":
                        m[rn][cn] = "^"
                    else:
                        m[rn][cn - 1]= "<"
                        m[rn][cn] = "X" 
                    
                elif m[rn][cn] == ">":
                    if rn == len(m[rn]) - 1:
                        m[rn][cn] = "X"
                        out = True
                    elif m[rn][cn +1] == "#":
                        m[rn][cn] = "v"
                    else:
                        m[rn][cn +1] = ">"
                        m[rn][cn] = "X" 
                        
    count = 0 
    path = set()
    for rn in range(len(m)):
            for cn in range(len(m[rn])):
                if m[rn][cn] == "X":
                    count += 1
                    path.add((rn, cn))
    print(count)
    return path

path = part1(m)
start = []

with open("./input.txt", "r") as f:
    lines = f.readlines()
    m = [list(line.strip()) for line in lines]

for rn in range(len(m)):
        for cn in range(len(m[rn])):
            if m[rn][cn] == "^":
                start = (rn, cn)
print(start)

path.remove(start)

p2 = 0
for (r, c) in path:
    m = []
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        m = [list(line.strip()) for line in lines]

    old_r = start[0]
    old_c = start[1]
    d = 0
    dxs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx = dxs[d]
    seen = set()
    

    m[r][c] = "#"
    while True:
        if (old_r, old_c, dx) in seen:
            p2 += 1
            break
      
        seen.add((old_r, old_c, dx))
        
        new_r = old_r + dx[0]    
        new_c = old_c + dx[1]

        if not (0<= new_r < len(m) and 0 <= new_c < len(m[0])):
            break

        if m[new_r][new_c] == "#":
            d = (d + 1) % 4
            dx = dxs[d]
            continue
        
        old_r = new_r
        old_c = new_c

print(p2)






