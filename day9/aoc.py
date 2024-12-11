with open("input.txt", "r") as f:
    dm = f.read()

ls = []
counter = 0
for i, d in enumerate(dm):
    if i % 2 == 0:
        for _ in range(int(d)):
            ls.append(counter)
        
        counter += 1
    
    else:
        for _ in range(int(d)):
            ls.append(".")



l = -1

for i , c in enumerate(ls):
    if i > len(ls) +l -1:
        break
    if c == ".":
        for ri, rc in enumerate(ls[l::-1]):
            if str(rc).isdigit():
                if i > len(ls) +l -1:
                    break
                ls[i] = rc
                ls[l] = "."
                l -= 1
                break
            else:
                l-=1
                continue
print(ls)
total = 0
for i, n in enumerate(ls):
    if n == ".":
        break

    total += i*int(n)       
    
print(total)



        
        
        
           
