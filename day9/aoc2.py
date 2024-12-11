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


