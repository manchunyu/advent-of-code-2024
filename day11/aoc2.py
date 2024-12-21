arr = "4 4841539 66 5279 49207 134 609568 0"

numbers = list(map(int, arr.split()))

total = 0
for _ in range(75):
    new = []
    for n in numbers:
        if len(str(n)) % 2 == 0:
            s = str(n)
            half = int(len(s)/2) 
            new.append(int(s[:half]))
            new.append(int(s[half:]))
        elif n == 0:
            new.append(1)
        else:
            new.append(n * 2024)

    numbers = new
    
print(len(numbers))
