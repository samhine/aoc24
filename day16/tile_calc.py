## This worked much faster for Part 1, but ended up not being too suitable for Part 2

from collections import defaultdict

with open("input.txt", "r") as file:
    maze = file.read().splitlines()
    maze = [list(x) for x in maze]

start = [(x, y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "S"][0]
end = [(x, y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "E"][0]

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

punishments = {
    ("N", "N"): 0,
    ("E", "E"): 0,
    ("S", "S"): 0,
    ("W", "W"): 0,
    ("N", "E"): 1,
    ("E", "S"): 1,
    ("S", "W"): 1,
    ("W", "N"): 1,
    ("E", "N"): 1,
    ("S", "E"): 1,
    ("W", "S"): 1,
    ("N", "W"): 1,
    ("N", "S"): 2,
    ("E", "W"): 2,
    ("S", "N"): 2,
    ("W", "E"): 2
}

scores = defaultdict(tuple)
scores[start] = (0, "E")

def populate_neighbours(position, scores):
    my_score = scores[position]
    x, y = position
    updated = []
    for direction in dirs:
        dx, dy = dirs[direction]
        if maze[y+dy][x+dx] == "." or maze[y+dy][x+dx] == "E":
            score = my_score[0] + 1 + punishments[(my_score[1], direction)]*1000
            if (x+dx, y+dy) not in scores or scores[(x+dx, y+dy)][0] > score:
                scores[(x+dx, y+dy)] = (score, direction)
                updated.append((x+dx, y+dy))

    return updated

def print_maze(maze, scores):
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if (x, y) in scores:
                row += scores[(x, y)][1]
            else:
                row += maze[y][x]
        print(row)

recently_updated = [start]

# This currently means that we end for the first score, rather than ensuring we've explored all routes

while len(recently_updated) > 0:
    updated = []
    for position in recently_updated:
        new = populate_neighbours(position, scores)
        updated.extend(new)
    
    recently_updated = updated

print(scores)
print_maze(maze, scores)
print(scores[(end[0], end[1])][0])

## Couldn't really find a good way to count routes here... so had to go back to slow slow BFS in main.py