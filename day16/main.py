from collections import defaultdict

with open("input.txt", "r") as file:
    maze = file.read().splitlines()
    maze = [list(x) for x in maze]

def have_been(pos, route):
    for r in route:
        if r[0] == pos[0] and r[1] == pos[1]:
            return True
    return False

def calculate_route(route):
    turns = 0
    steps = 0
    facing = 'E'
    for step in route:
        if step[2] != facing:
            turns += 1
            facing = step[2]
        steps += 1
    
    return 1000*turns + steps - 1

def cull_routes(routes):
    # for each route, check if another route has the same position, but a lower score
    # if so, remove the route

    for idx, route in enumerate(routes):
        for other_route in routes:
            if route != other_route:
                if route[-1] in other_route:
                    if calculate_route(route) > calculate_route(other_route):
                        routes.pop(idx)
                        break
    
    return routes

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

start = [(x, y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "S"][0]
end = [(x, y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "E"][0]

routes = []
completed_routes = []

for dir in dirs:
    if maze[start[1]+dirs[dir][1]][start[0]+dirs[dir][0]] != "#":
        routes.append([(start[0], start[1], dir)])

print(routes)

reached = defaultdict(lambda:999999999999999999)

# BFS
while len(routes) > 0:
    new_routes = []
    for idx, route in enumerate(routes):
        pos = route[-1]
        if pos[0] == end[0] and pos[1] == end[1]:
            completed_routes.append(route)
        else:
            for dir in dirs:
                new_pos = (pos[0]+dirs[dir][0], pos[1]+dirs[dir][1], dir)
                if not have_been(new_pos, route) and maze[new_pos[1]][new_pos[0]] != "#":
                    new_route = route + [new_pos]
                    score = calculate_route(new_route)
                    # Only append a new route if it hasn't been reached before with a lower score
                    if score <= reached[new_pos]:
                        reached[new_pos] = score
                        new_routes.append(new_route)

    print(len(new_routes))
    routes = new_routes

# print(completed_routes)
# print(len(completed_routes))

best=min([calculate_route(route) for route in completed_routes])

# Part 1
print(best)

shortest_routes = [route for route in completed_routes if calculate_route(route) == best]
visited = set()
for route in shortest_routes:
    for pos in route:
        visited.add((pos[0], pos[1]))

# Part 2
print(len(visited))