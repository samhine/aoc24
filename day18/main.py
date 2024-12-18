with open("input.txt", "r") as file:
    input = file.read().splitlines()
    coords = []
    for row in input:
        x,y = row.split(',')
        coords.append((int(x),int(y)))

# first_1024 = coords[:1024]

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Calculate maze based on how many "steps" we've already taken
        # maze = maze_at_sec(current_node.g-1, coords)

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def maze_at_sec(sec, coords):
    maze = []
    relevant_coords = coords[:sec]
    for y in range(height):
        row = []
        for x in range(width):
            if (x,y) in relevant_coords:
                row.append(1)
            else:
                row.append(0)
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
end = (70, 70)
bits = 750

maze = maze_at_sec(bits, coords)
print_maze(maze)
path = astar(maze, start, end)
print(path)
print(len(path))
print_path(maze, path)