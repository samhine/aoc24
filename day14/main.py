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
    
    with open("output.txt", "a") as file:
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

found = False

while not found:
    positions = set()
    for robot in robots:
        raw_pos = (robot["p"][0]+robot["v"][0]*seconds, robot["p"][1]+robot["v"][1]*seconds)
        positions.add((raw_pos[0] % width, raw_pos[1] % height))
    
    # Check for row of 30 consecutive points
    for pos in positions:
        exists = True
        for i in range(1, 30):
            if (pos[0]+i, pos[1]) not in positions:
                exists = False
                break
        
        if exists:
            print(f"Found at {pos} after {seconds} seconds")
            output_map(robots, seconds)
            break

    seconds += 1


    