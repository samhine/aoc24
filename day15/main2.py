with open("input.txt", "r") as file:
    input = file.read().split("\n\n")
    warehouse = [list(x) for x in input[0].splitlines()]
    orders = [x for x in input[1] if x in "<>^v"]

    resized_warehouse = []
    for y in range(len(warehouse)):
        new_row = []
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "#":
                new_row += ["#", "#"]
            elif warehouse[y][x] == ".":
                new_row += [".", "."]
            elif warehouse[y][x] == "@":
                new_row += ["@", "."]
            elif warehouse[y][x] == "O":
                new_row += ["[", "]"]
        resized_warehouse.append(new_row)
    
    warehouse = resized_warehouse

print(warehouse)
print(orders)

dirs = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}
robot_pos = [(x, y) for y in range(len(warehouse)) for x in range(len(warehouse[0])) if warehouse[y][x] == '@'][0]

# returns index of free space
def can_move_horizontal(pos, dir, warehouse=warehouse):
    check_pos = (pos[0] + dir[0], pos[1] + dir[1])
    while check_pos[0] >= 0 and check_pos[0] < len(warehouse[0]) and check_pos[1] >= 0 and check_pos[1] < len(warehouse):
        if warehouse[check_pos[1]][check_pos[0]] == ".":
            return check_pos
        if warehouse[check_pos[1]][check_pos[0]] == "#":
            return False
        check_pos = (check_pos[0] + dir[0], check_pos[1] + dir[1])

    return False

def find_box_neighbours(box, dir, warehouse=warehouse):
    neighbouring_boxes = [box]

    # [] is box
    # [ is left, ] is right
    # left_neighbour is the position in the dir of the left box
    # right_neighbour is the position in the dir of the right box

    left, right = box
    left_neighbour = (left[0] + dir[0], left[1] + dir[1])
    right_neighbour = (right[0] + dir[0], right[1] + dir[1])

    if warehouse[left_neighbour[1]][left_neighbour[0]] == "[":
        this_box = (left_neighbour, (left_neighbour[0] + 1, left_neighbour[1]))
        neighbouring_boxes.extend(find_box_neighbours(this_box, dir))
    elif warehouse[left_neighbour[1]][left_neighbour[0]] == "]":
        this_box = ((left_neighbour[0] - 1, left_neighbour[1]), left_neighbour)
        neighbouring_boxes.extend(find_box_neighbours(this_box, dir))
    
    if warehouse[right_neighbour[1]][right_neighbour[0]] == "[": 
        this_box = (right_neighbour, (right_neighbour[0] + 1, right_neighbour[1]))
        neighbouring_boxes.extend(find_box_neighbours(this_box, dir))
    elif warehouse[right_neighbour[1]][right_neighbour[0]] == "]":
        this_box = ((right_neighbour[0] - 1, right_neighbour[1]), right_neighbour)
        neighbouring_boxes.extend(find_box_neighbours(this_box, dir))
    
    return neighbouring_boxes

def can_move_vertical(pos, dir, warehouse=warehouse):
    boxes = []
    free_space = None
    check_pos = (pos[0] + dir[0], pos[1] + dir[1])
    while check_pos[0] >= 0 and check_pos[0] < len(warehouse[0]) and check_pos[1] >= 0 and check_pos[1] < len(warehouse):
        if warehouse[check_pos[1]][check_pos[0]] == ".":
            free_space = check_pos
            print("Free space", free_space)
            break
        elif warehouse[check_pos[1]][check_pos[0]] == "#":
            return False, []
        elif warehouse[check_pos[1]][check_pos[0]] == "[":
            boxes.append((check_pos, (check_pos[0] + 1, check_pos[1])))
        elif warehouse[check_pos[1]][check_pos[0]] == "]":
            boxes.append(((check_pos[0] - 1, check_pos[1]), check_pos))
        check_pos = (check_pos[0] + dir[0], check_pos[1] + dir[1])

    if free_space is None:
        return False, []

    # check boxes for any unfound neighbours
    print("Naive affected boxes", boxes)
    affected_boxes = []
    for box in boxes:
        affected_boxes.extend(find_box_neighbours(box, dir))
    affected_boxes = list(set(affected_boxes))
    
    for box in affected_boxes:
        # if the position in dir of either side of the box is not free, we can't move
        if warehouse[box[0][1]+dir[1]][box[0][0]] == "#" or warehouse[box[1][1]+dir[1]][box[1][0]] == "#":
            return False, []
        
    return free_space, affected_boxes
    

def move_vertical(pos, dir, free_pos, boxes):
    if boxes:
        target_y = max([box[0][1] for box in boxes]) if dir[1] == 1 else min([box[0][1] for box in boxes])
    else:
        target_y = pos[1]

    # for each row, moving from our target row to our robot row
    print("Loop info", target_y, pos[1], -dir[1])
    for y in range(target_y, pos[1], -dir[1]):
        # for each box, if this box sits on this row, move it
        for box in boxes:
            if box[0][1] == y:
                warehouse[box[0][1]][box[0][0]] = "."
                warehouse[box[1][1]][box[1][0]] = "."
                warehouse[box[0][1] + dir[1]][box[0][0]] = "["
                warehouse[box[1][1] + dir[1]][box[1][0]] = "]"
    
    # move our robot
    warehouse[pos[1]][pos[0]] = "."
    warehouse[pos[1]+dir[1]][pos[0]] = "@"

    return (pos[0], pos[1] + dir[1]), warehouse
    

def move_horizonal(pos, dir, free_pos):
    print(pos, dir, free_pos)
    curr_pos = free_pos
    while curr_pos != pos:
        replace_pos = (curr_pos[0] - dir[0], curr_pos[1] - dir[1])
        warehouse[curr_pos[1]][curr_pos[0]] = warehouse[replace_pos[1]][replace_pos[0]]
        curr_pos = replace_pos
    warehouse[pos[1]][pos[0]] = "."
    return (pos[0] + dir[0], pos[1] + dir[1]), warehouse

def print_warehouse(warehouse):
    for row in warehouse:
        print("".join(row))

def calculate_gps(warehouse):
    gps = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "[":
                gps += x + 100*y
    return gps

def count_boxes(warehouse):
    count = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "[":
                count += 1
    return count

print("Start")
print_warehouse(warehouse)
for idx, order in enumerate(orders):
    if order in "<>":
        maybe_move = can_move_horizontal(robot_pos, dirs[order])
        # print(maybe_move)
        if maybe_move is not False:
            robot_pos, warehouse = move_horizonal(robot_pos, dirs[order], maybe_move)
    else:
        maybe_move, affected_boxes = can_move_vertical(robot_pos, dirs[order])
        print("Affected boxes", affected_boxes)
        if maybe_move is not False:
            robot_pos, warehouse = move_vertical(robot_pos, dirs[order], maybe_move, affected_boxes)
    print(f"Order {order}")
    print_warehouse(warehouse)
    print("Boxes", count_boxes(warehouse))

print(calculate_gps(warehouse))