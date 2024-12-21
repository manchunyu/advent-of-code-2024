garden = []
with open("input.txt", "r") as f:
    rows = f.readlines()
    for row in rows:
        garden.append(row.strip())

R = len(garden)
C = len(garden[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

seen = set()

for o_r in range(R):
    for o_c in range(C):
        if (o_r, o_c) in seen:
            continue
        seen.add((o_r, o_c))
        


