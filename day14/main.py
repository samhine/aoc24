with open("input.txt", "r") as file:
    height = 7
    width = 11
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
second = 0

possible = []
found = False

while not found:
    positions = set()
    quadrants = {
        "tl": 0,
        "tr": 0,
        "bl": 0,
        "br": 0
    }
    for robot in robots:
        raw_pos = (robot["p"][0]+robot["v"][0]*second, robot["p"][1]+robot["v"][1]*second)
        robot["p"] = (raw_pos[0] % width, raw_pos[1] % height)
        positions.add(robot["p"])
    
    for x in range(width):
        for y in range(height):
            if (x, y) in positions:
                if x < width//2 and y < height//2:
                    quadrants["tl"] += 1
                elif x > width//2 and y < height//2:
                    quadrants["tr"] += 1
                elif x < width//2 and y > height//2:
                    quadrants["bl"] += 1
                elif x > width//2 and y > height//2:
                    quadrants["br"] += 1
    
    if quadrants["tl"] == quadrants["tr"] and quadrants["bl"] == quadrants["br"]:
        # Check if the right had side of the map is a mirror image of the left
        # symmetrical = True
        # for each in robots:
        #     # If for each point (< width//2), there exists another point flipped across width//2 (on the same y) then we have a match
        #     if each["p"][0] < width//2 and (width-each["p"][0], each["p"][1]) in positions:
        #         continue
        #     else:
        #         symmetrical = False
        #         break
        # if symmetrical:
        #     found = True
        #     print(second)
        #     output_map(robots, second)
        output_map(robots, second)
    second += 1


    