m = [] 
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        m.append(line.replace("\n", ""))

print(m)
R = len(m)
C = len(m[0])    
antennas = set()
for r in range(R):
    for c in range(C):
        if m[r][c].isalnum():
            antennas.add((m[r][c], r , c))


antennas = sorted(antennas, key=lambda a: (a[1], a[2]))
print(antennas)     

marked = set()
for i , (aa, rr, cc) in enumerate(antennas):
    o_c = cc
    o_r = rr
    for (a, r, c) in antennas[i+ 1:]:
        if aa != a:
            continue
        cc = o_c
        rr = o_r

        dr = r- rr
        dc = c - cc

        adr = abs(dr)
        adc = abs(dc)
        if dc > 0:
            while (0 <= rr < R and 0 <= cc < C):
                marked.add((rr, cc))
                rr -= adr
                cc -= adc

            while (0 <= r < R and 0 <= c < C):
                marked.add((r , c))
                r += adr
                c += adc

        else:
            while (0 <= rr < R and 0 <= cc < C):
                marked.add((rr, cc))
                rr -= adr
                cc += adc

            while (0 <= r < R and 0 <= c < C):
                marked.add((r , c))
                r += adr
                c -= adc


print(len(marked))
    