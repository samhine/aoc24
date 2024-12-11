from multiprocessing import Process

with open("input.txt", "r") as file:
    stones = file.read().split()
    stones = [int(x) for x in stones]
print(stones)
blinks = 75

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def process_stones(stones):
    new_stones = []
    for idx, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0: # Anyway to get rid of the string?
            split_stone = [int(x) for x in list(split(str(stone), 2))]
            new_stones += split_stone
        else:
            new_stones.append(int(stone)*2024)
    return new_stones

for i in range(blinks):  
    new_stones = process_stones(stones)
    stones = new_stones

print(len(stones))