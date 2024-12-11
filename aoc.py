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
            
            r, c = o_r, o_c
            paths = set((0, r, c))
            
            for i in range(1, 10):  
                found = False         
                for path in paths:                                     
                    for d in range(4):
                        rr = r + directions[d][0]
                        cc = c + directions[d][1]
                        if (0 <= rr < R and 0 <= cc < C):
                            if int(G[rr][cc]) == i and found == False:
                                found = True
                                paths = set()
                                paths.add((i, rr, cc)) 
                            elif int(G[rr][cc]) == i and found == True:
                                paths.add((i, rr, cc)) 

            for c in paths:
                if c[0] == 9:
                    score += 1


print(score)


            
