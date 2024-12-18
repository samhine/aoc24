from collections import defaultdict
from astar import a_star_search

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
                row.append(0)
            else:
                row.append(1)
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

width = 71
height = 71

start = (0, 0)
end = (width-1, height-1)

## Part 1
maze = maze_at_sec(1024, coords)
path, path_length = a_star_search(maze, start, end)
print(path_length-1) # Don't count 0th step

## Part 2

# Could binary search here but I'm lazy
for i in range(len(coords)):
    bits = i
    maze = maze_at_sec(bits, coords)

    path, path_length = a_star_search(maze, start, end)
    if not path:
        print(coords[i-1])
        break
