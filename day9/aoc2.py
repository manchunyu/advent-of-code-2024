dm =""
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



index = 0

      

rls = ls[::-1]
# print(rls[-3])
# print(rls[-2:0 +2 -1:-1])

prev = ""

for ri, rc in enumerate(rls):
    # print(f"ri: {ri}, rc: {rc}")
    if str(rc).isdigit() and rc != prev:
        digit_count = 0
        
        for rcc in rls[ri:]:
            if rcc == rc:
                digit_count += 1
            else:
                break
        
        for i, c in enumerate(rls[:ri+digit_count-1:-1]):
            dot_count = 0           
            if c == ".":              
                for cc in rls[-i-1:ri+digit_count-1:-1]:
                    if cc == ".":
                        dot_count += 1
                    else:
                        break
                if dot_count >= digit_count:
                    for n in range(digit_count):
                        rls[-i-n-1] = rc
                        rls[ri + n ] = "."
                    
                    break
                else:
                    prev = rc
                    continue

    else:
        continue

final_ls  = rls[::-1]
total = 0
for i, c in enumerate(final_ls):
    if str(c).isdigit():
        total += c * i
    else:
        continue

print(total)




                
                    




# -------------------------------------------

# for ri , rc in enumerate(ls[::-1]):
#     print(f"ri: {ri}, rc: {rc}")
#     if str(rc).isdigit():
#         digit_count = 0
        
#         for rcc in ls[l - ri::-1]:            
#             if rcc == rc:
#                 digit_count += 1
#             else:
#                 break
#         for i , c in enumerate(ls[:l-digit_count]):
#             if c == ".":
#                 dot_count = 0
#                 for cc in ls[i:l-digit_count]:
#                     if cc == ".":
#                         dot_count += 1
#                     else:
#                         break
#                 if dot_count >= digit_count:
#                     for n in range(digit_count):
#                         ls[i+n] = rc
#                         ls[l- ri - n] = "."
                        
#                     l -= (ri + digit_count)
#                     break
#                 else:
#                     continue
#     else:
#         l -= 1
#         continue







