from collections import defaultdict

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    coords = []
    for row in input:
        x,y = row.split(',')
        coords.append((int(x),int(y)))

def maze_at_sec(sec, coords):
    maze = []
    relevant_coords = coords[:sec]
    for y in range(height):
        row = []
        for x in range(width):
            if (x,y) in relevant_coords:
                row.append('#')
            else:
                row.append('.')
        maze.append(row)
    
    return maze

def print_maze(maze):
    for row in maze:
        p = ["." if c==0 else "#" for c in row]
        print("".join(p))

def print_path(maze, path):
    for rc, row in enumerate(maze):
        prow = ""
        for cc, col in enumerate(row):
            if (cc, rc) in path:
                prow += "O"
            elif col == 1:
                prow += "#"
            else:
                prow += "."
        print(prow)

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

def populate_neighbours(maze, position, scores):
    my_score = scores[position]
    x, y = position
    updated = []
    for direction in dirs:
        dx, dy = dirs[direction]
        new_pos = (x+dx, y+dy)
        if new_pos[0] < 0 or new_pos[0] >= width or new_pos[1] < 0 or new_pos[1] >= height:
            continue

        if maze[y+dy][x+dx] == ".":
            score = my_score + 1
            if new_pos not in scores or scores[(x+dx, y+dy)] > score:
                scores[(x+dx, y+dy)] = score
                updated.append((x+dx, y+dy))
    return maze, updated, scores

def tile_map(maze, start, end):
    recently_updated = [start]
    scores = defaultdict(int)

    while len(recently_updated) > 0:
        updated = []
        for position in recently_updated:
            maze, new, scores = populate_neighbours(maze, position, scores)
            updated.extend(new)
        
        recently_updated = updated
    
    return scores

width = 71
height = 71

start = (0, 0)
end = (width-1, height-1)

## Part 1
maze = maze_at_sec(1024, coords)
scores = tile_map(maze, start, end)
print(scores[end])

## Part 2

# Could binary search here but I'm lazy
for i in range(len(coords)):
    bits = i
    maze = maze_at_sec(bits, coords)

    scores = tile_map(maze, start, end)
    if end not in scores:
        print(coords[i-1])
        break
