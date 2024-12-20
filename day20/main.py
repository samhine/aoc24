from collections import defaultdict
from copy import deepcopy

with open("input.txt") as file:
    file = file.read().splitlines()
    maze = [list(row) for row in file]

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def populate_neighbours(maze, position, scores):
    my_score = scores[position]
    x, y = position
    updated = []
    for direction in dirs:
        dx, dy = dirs[direction]
        new_pos = (x+dx, y+dy)
        if new_pos[0] < 0 or new_pos[0] >= len(maze[0]) or new_pos[1] < 0 or new_pos[1] >= len(maze):
            continue

        if maze[y+dy][x+dx] == "." or maze[y+dy][x+dx] == "E":
            score = my_score + 1
            if new_pos not in scores or scores[(x+dx, y+dy)] > score:
                scores[(x+dx, y+dy)] = score
                updated.append((x+dx, y+dy))
    return maze, updated, scores

def tile_map(maze, start):
    recently_updated = [start]
    scores = defaultdict(int)

    while len(recently_updated) > 0:
        updated = []
        for position in recently_updated:
            maze, new, scores = populate_neighbours(maze, position, scores)
            updated.extend(new)
        
        recently_updated = updated
    
    return scores

base_maze = maze.copy()
start = [(x,y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "S"][0]
end = [(x,y) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == "E"][0]
base_scores = tile_map(base_maze, start)
base_score = base_scores[end]

# Part 1

seconds_saved = defaultdict(int)
for score in base_scores:
    for other_score in base_scores:
        if manhattan_distance(score, other_score) <= 2 and base_scores[other_score] > base_scores[score]:
            seconds_saved[base_scores[other_score] - base_scores[score] - manhattan_distance(score, other_score)] += 1

cutoff = 100
print(sum([val for key, val in seconds_saved.items() if key >= cutoff]))

# Part 2

seconds_saved = defaultdict(int)
for score in base_scores:
    for other_score in base_scores:
        if manhattan_distance(score, other_score) <= 20 and base_scores[other_score] > base_scores[score]:
            seconds_saved[base_scores[other_score] - base_scores[score] - manhattan_distance(score, other_score)] += 1

cutoff = 100
print(sum([val for key, val in seconds_saved.items() if key >= cutoff]))