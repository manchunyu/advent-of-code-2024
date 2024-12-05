import math
rules = {}

with open("rules.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a, b= line.split("|")
        if b.strip("\n") in rules:
            rules[b.strip("\n")].append(a)
        else:
            rules[b.strip("\n")] = [a]
print(rules)
lines = []
f = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        n = []
        for num in line:
            if not n:
                n.append(num)
                continue
            ok = True
            for i in n:             
                if i not in rules.get(num, []):
                    ok = False
            if ok:
                n.append(num)         
        if len(n) != len(line):
            f.append(line)

def nsort(l):
    ls = []
    for i in l:
        ls.append(i)
    new = []
    for i in range(len(l)-1):
        if l[i + 1] in rules.get(l[i], []):
            tmp = l[i]
            l[i] = l[i+1]
            l[i+1] = tmp
            new.append(l[i])
        else:
            new.append(l[i])
    new.append(l[len(l)-1])
    if ls == new:
        return new
    else:
        return nsort(new)
    

        


total = 0
for l in f:
    print(len(l))
    l = nsort(l)
    print(l)
    # l.sort(key = lambda i: len(rules.get(i, [])))
    
    total += int(l[math.floor(len(l)/2)])
print(total)

                
            
    
