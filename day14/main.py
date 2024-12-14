with open("input.txt", "r") as file:
    height = 103
    width = 101
    input = file.read().splitlines()

def parse_input(row):
    refined = row.replace("p=", "").replace("v=", "")
    p, v = refined.split()
    return {
        "p": (int(p.split(",")[0]), int(p.split(",")[1])),
        "v": (int(v.split(",")[0]), int(v.split(",")[1]))
    }

def output_map(robot, seconds):
    map = [["." for x in range(width)] for y in range(height)]
    for robot in robots:
        map[robot["p"][1]][robot["p"][0]] = "#"
    
    with open("output.txt", "w+") as file:
        file.write(f"Seconds: {seconds}\n")
        for row in map:
            file.write("".join(row) + "\n")
        

robots = [parse_input(row) for row in input]
seconds = 100

quadrants = {
    "tl": 0,
    "tr": 0,
    "bl": 0,
    "br": 0
}

for robot in robots:
    raw_pos = (robot["p"][0]+robot["v"][0]*seconds, robot["p"][1]+robot["v"][1]*seconds)
    robot["p"] = (raw_pos[0] % width, raw_pos[1] % height)
    if robot["p"][0] < width//2 and robot["p"][1] < height//2:
        quadrants["tl"] += 1
    elif robot["p"][0] > width//2 and robot["p"][1] < height//2:
        quadrants["tr"] += 1
    elif robot["p"][0] < width//2 and robot["p"][1] > height//2:
        quadrants["bl"] += 1
    elif robot["p"][0] > width//2 and robot["p"][1] > height//2:
        quadrants["br"] += 1

tot = 1
for v in quadrants.values():
    tot *= v

print(tot)

robots = [parse_input(row) for row in input]
seconds = 0

possible = []
found = False

tree_shape = [
    (0,0),
    (-1,1),
    (1,1),
    (-2,2),
    (2,2),
    (-3,3),
    (3,3),
    (-4,4),
    (4,4)
]

while not found:
    positions = set()
    for robot in robots:
        raw_pos = (robot["p"][0]+robot["v"][0]*seconds, robot["p"][1]+robot["v"][1]*seconds)
        robot["p"] = (raw_pos[0] % width, raw_pos[1] % height)
        positions.add(robot["p"])
    
    for pos in positions:
        # Check if the tree shape is present in the positions
        if pos[0] < 4 or pos[1] > height-4:
            continue
        
        exists = True
        for tree in tree_shape:
            if (pos[0]+tree[0], pos[1]+tree[1]) not in positions:
                exists = False
                break
        
        if exists:
            print("Found at ", pos)
            print("Seconds: ", seconds)
            output_map(robots, seconds)
            found = True
            break

    seconds += 1


    