with open("input.txt", "r") as file:
    lines = file.readlines()

results = []
nums = []

for line in lines:
    result, num = line.replace("\n", "").split(": ")
    results.append(int(result))
    nums.append(num.split(" "))


p1 = 0
for ns in range(len(nums)):  
    prev = [nums[ns][0]]
    for n in nums[ns][1: ]:
        n = int(n)
        current = []       
        for num in prev:
            num = int(num)
            current.append(num + n)
            current.append(num * n) 
            current.append(int(str(num) +str(n)))      
        prev = current
    if results[ns] in prev:
        p1 += results[ns]
    
print(p1)
    

            


            

        

    