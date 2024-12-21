G = []
with open("input.txt", "r") as f:
    rows = f.readlines()
    for row in rows:
        G.append(row.strip())

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R = len(G)
C = len(G[0])

score = 0
for o_r in range(R):
    for o_c in range(C):
        if int(G[o_r][o_c]) == 0:
            
            (r, c) = (o_r, o_c)
            start = (int(G[r][c]), r, c)
            current = [start]
            
            path_ahead = []
                       
            
            for i in range(1, 10):
                for path in current:                   
                    for d in range(4):                                     
                        rr = path[1] + directions[d][0]
                        cc = path[2] + directions[d][1]
                        if (0 <= rr < R and 0 <= cc < C):
                            if int(G[rr][cc]) == i:
                                path_ahead.append((int(G[rr][cc]), rr, cc))
                            
                current = path_ahead
                path_ahead = []

            
            for p in current:
                if p[0] == 9:
                    score += 1
                           
        else:
            continue             


print(score)


            
