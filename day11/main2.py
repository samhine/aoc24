# After 3 iterations
# 0 ->3 20,24
# 1 ->3 2,0,2,4
# x ->1 x*2024 ->2 

from multiprocessing import Process

with open("input.txt", "r") as file:
    stones = file.read().split()

print(stones)
blinks = 25

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def process_stones(stones):
    new_stones = []
    for idx, stone in enumerate(stones):
        if stone == "0":
            new_stones += ['20', '24']
        elif stone == "1":
            new_stones += ['2', '0', '2', '4']
        elif len(stone) % 4 == 0:
            split_stone = [str(int(x)) for x in list(split(stone, 4))]
            new_stones += split_stone
        elif len(stone) % 2 == 0:
            split_stone = [str(int(x)) for x in list(split(stone, 2))]
            new_stones += split_stone
        else:
            x = str(int(stone)*2024)
            new_stones+=process_stones([x])
    return new_stones

for i in range(blinks):
    
    new_stones = process_stones(stones)
    stones = new_stones

print(len(stones))