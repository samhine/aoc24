import copy

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    input = [list(x) for x in input]

guard_pos = [(x,y) for x in range(len(input[0])) for y in range(len(input)) if input[y][x] == "^"][0]

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

def guard_run(input, guard_pos):
    dir = "N"
    visited = [guard_pos]
    while guard_pos[0]+dirs[dir][0] > 0 and guard_pos[1]+dirs[dir][1] > 0 and guard_pos[0]+dirs[dir][0] < len(input[0]) and guard_pos[1]+dirs[dir][1] < len(input):
        if input[guard_pos[1]+dirs[dir][1]][guard_pos[0]+dirs[dir][0]] != "#":
            guard_pos = (guard_pos[0]+dirs[dir][0], guard_pos[1]+dirs[dir][1])
            visited.append(guard_pos)
        else:
            match dir:
                case "N":
                    dir = "E"
                case "E":
                    dir = "S"
                case "S":
                    dir = "W"
                case "W":
                    dir = "N"
    return visited

def guard_loop(input, guard_pos):
    dir = "N"
    visited = [guard_pos]
    moved_without_update = 0
    while guard_pos[0]+dirs[dir][0] > 0 and guard_pos[1]+dirs[dir][1] > 0 and guard_pos[0]+dirs[dir][0] < len(input[0]) and guard_pos[1]+dirs[dir][1] < len(input):
        if input[guard_pos[1]+dirs[dir][1]][guard_pos[0]+dirs[dir][0]] != "#":
            guard_pos = (guard_pos[0]+dirs[dir][0], guard_pos[1]+dirs[dir][1])
            before = len(set(visited))
            visited.append(guard_pos)
            after = len(set(visited))

            print(visited)

            if before == after:
                moved_without_update += 1
                if moved_without_update == before:
                    return 1
        else:
            match dir:
                case "N":
                    dir = "E"
                case "E":
                    dir = "S"
                case "S":
                    dir = "W"
                case "W":
                    dir = "N"
    return 0

visited = guard_run(input, guard_pos)

print(set(visited))
print(len(list(set(visited))))

count = 0
for pos in visited:
    print(pos)
    x, y = pos
    if input[y][x] == "^":
        continue
    check_input = copy.deepcopy(input)
    check_input[y][x] = "#"
    count += guard_loop(check_input, guard_pos)

print(count)