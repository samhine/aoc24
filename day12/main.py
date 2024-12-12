from collections import defaultdict

with open('input.txt', 'r') as file:
    input = file.read().splitlines()
    input = [list(x) for x in input]

categorised = []
regions = []

dirs = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

def count_consectutive_runs(arr):
    runs = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]+1:
            runs += 1
    return runs

def calc_sides(region):
    perimeters = {
        "up": [],
        "down": [],
        "left": [],
        "right": []
    }
    for pos in region:
        for direction in ["up", "down", "left", "right"]:
            new_pos = (pos[0]+dirs[direction][0], pos[1]+dirs[direction][1])
            if new_pos not in region:
                perimeters[direction].append(pos)

    slices = {
        "up": defaultdict(list),
        "down": defaultdict(list),
        "left": defaultdict(list),
        "right": defaultdict(list)
    }

    sides = 0

    for direction, perim in perimeters.items():
        for point in perim:
            if direction in ["up", "down"]:
                slices[direction][point[1]].append(point[0])
            else:
                slices[direction][point[0]].append(point[1])
    
    for direction, slice in slices.items():
        for row, perim in slice.items():
            perim.sort()
            sides += count_consectutive_runs(perim)
    
    return sides

def calc_perimeter(region):
    perimeter = 0
    for pos in region:
        for direction, dir in dirs.items():
            new_pos = (pos[0]+dir[0], pos[1]+dir[1])
            if new_pos not in region:
                perimeter += 1
    return perimeter

def calc_area(region):
    return len(region)

def explore_region(x, y, letter):
    expored = []
    unexplored = [(x, y)]

    while len(unexplored) > 0:
        current = unexplored.pop()
        expored.append(current)
        for direction, pos in dirs.items():
            new_pos = (current[0]+pos[0], current[1]+pos[1])
            if new_pos in expored:
                continue
            if new_pos[0] < 0 or new_pos[0] >= len(input[0]) or new_pos[1] < 0 or new_pos[1] >= len(input):
                continue
            if input[new_pos[1]][new_pos[0]] == letter:
                unexplored.append(new_pos)

    return expored

tot = 0
for x in range(len(input[0])):
    for y in range(len(input)):
        if (x, y) in categorised:
            continue
        region = explore_region(x, y, input[y][x])
        categorised += region
        tot += calc_area(set(region)) * calc_sides(set(region))
        regions.append(set(region))

# for region in regions:
#     print(region)
#     print(calc_sides(set(region)))
#     print(calc_area(region), calc_sides(region))

print(tot)
