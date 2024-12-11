from collections import defaultdict

with open("input.txt", "r") as file:
    stones = file.read().split()
    stones = [int(x) for x in stones]

print(stones)
blinks = 75

def process_stone(stone):
    str_stone = str(stone)
    if stone == 0:
        return [1]
    elif len(str_stone) % 2 == 0:
        return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]
    else:
        return [stone*2024]
    
def process_stones(stone_dict):
    final_stone_dict = defaultdict(int)

    for stone, count in stone_dict.items():
        processed_stones = process_stone(stone)
        for p_stone in processed_stones:
            final_stone_dict[p_stone] += count
    
    return final_stone_dict

stone_dict = defaultdict(int)
for stone in stones:
    stone_dict[stone] += 1


for i in range(blinks):
    print(stone_dict)
    new_stone_dict = process_stones(stone_dict)
    stone_dict = new_stone_dict

print(sum([count for stone, count in stone_dict.items()]))