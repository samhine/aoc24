from collections import defaultdict
import copy

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    input = [list(x) for x in input]

routes = []
# find the root node (position with value 0) and build the tree from there
for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] == "0":
            routes.append([{
                "pos": (x, y),
                "value": 0
            }])


print(routes)

dirs = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

step = 1
while step<10:
    for route in routes:
        if len(route) == step:
            for direction, pos in dirs.items():
                old_pos = (route[-1]["pos"][0], route[-1]["pos"][1])
                new_pos = (route[-1]["pos"][0]+pos[0], route[-1]["pos"][1]+pos[1])
                if new_pos[0] < 0 or new_pos[0] >= len(input[0]) or new_pos[1] < 0 or new_pos[1] >= len(input):
                    continue
                if int(input[new_pos[1]][new_pos[0]]) - int(input[old_pos[1]][old_pos[0]]) == 1:
                    new_route = copy.deepcopy(route)
                    new_route.append({
                        "pos": new_pos,
                        "value": input[new_pos[1]][new_pos[0]]
                    })
                    routes.append(new_route)
    step += 1
    

part1 = False

trailheads = defaultdict(list) if part1 else defaultdict(int)
complete_routes = []

for route in routes:
    if len(route) == 10:
        if part1:
            trailheads[route[0]["pos"]].append(route[-1]["pos"])
        else:
            trailheads[route[0]["pos"]] += 1
        complete_routes.append(route)

print(trailheads)
for r in complete_routes:
    print(r)

if part1:
    for k,v in trailheads.items():
        trailheads[k] = set(v)

    print(sum([len(v) for v in trailheads.values()]))
else:
    print(sum([v for v in trailheads.values()]))
