arrangement = "4 4841539 66 5279 49207 134 609568 0"

stones = list(map(int, arrangement.split()))

cache = {}


def count(stone, blinks):
    if blinks == 0:
        return 1
    if (stone, blinks) not in cache:
        if stone == 0:
            result = count(1, blinks - 1)
            cache[(stone, blinks)] = result
            return result

        string = str(stone)
        length = len(string)

        if length % 2 == 0:
            result = count(int(string[:length // 2]), blinks - 1) + count(int(string[length// 2 :]), blinks - 1)       
        
        else:
            result = count(stone *2024, blinks - 1)
            
        cache[(stone, blinks)] = result
        return result
    else:
        return cache[((stone, blinks))]

print(sum(count(stone, 75) for stone in stones))

