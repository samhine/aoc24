with open("input.txt", "r") as file:
    input = file.read().splitlines()
    input = [list(x) for x in input]

def distance(p1, p2):
    return p1[0]-p2[0], p1[1]-p2[1]

map = dict()
for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] != ".":
            map[(x, y)] = input[y][x]

print(map)

locations = []
for x in range(len(input[0])):
    for y in range(len(input)):
        for antenee, char in map.items():
            dist = distance(antenee, (x, y))
            expected_ant = (x+2*dist[0], y+2*dist[1])
            if expected_ant in map and map[expected_ant] == char and antenee != expected_ant:
                locations.append((x, y))
                input[y][x] = "#"

for x in input:
    print("".join(x))

print(len(set(locations)))

locations = []
for x in range(len(input[0])):
    for y in range(len(input)):
        for antenee, char in map.items():
            dist = distance(antenee, (x, y))
            expected_ant = (x+2*dist[0], y+2*dist[1])
            if expected_ant in map and map[expected_ant] == char and antenee != expected_ant:
                locations.append((x, y))

                # When we find location we can append locations for every multiple of that distance going forwards
                counter = 0
                while x+counter*dist[0] < len(input[0]) and y+counter*dist[1] < len(input) and x+counter*dist[0] >= 0 and y+counter*dist[1] >= 0:
                    input[y+counter*dist[1]][x+counter*dist[0]] = "#"
                    locations.append((x+counter*dist[0], y+counter*dist[1]))
                    counter += 1
                
                # and backwards
                counter = 0
                while x-counter*dist[0] < len(input[0]) and y-counter*dist[1] < len(input) and x-counter*dist[0] >= 0 and y-counter*dist[1] >= 0:
                    input[y-counter*dist[1]][x-counter*dist[0]] = "#"
                    locations.append((x-counter*dist[0], y-counter*dist[1]))
                    counter += 1

                input[y][x] = "#"

# Ensure any antennas that appear twice are included
cs = [c for a, c in map.items()]
for a, c in map.items():
    if cs.count(c) > 1:
        locations.append(a)

for x in input:
    print("".join(x))

print(len(set(locations)))

