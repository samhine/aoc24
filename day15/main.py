with open("input.txt", "r") as file:
    input = file.read().split("\n\n")
    warehouse = [list(x) for x in input[0].splitlines()]
    orders = [x for x in input[1] if x in "<>^v"]

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
def can_move(pos, dir, warehouse=warehouse):
    check_pos = (pos[0] + dir[0], pos[1] + dir[1])
    while check_pos[0] >= 0 and check_pos[0] < len(warehouse[0]) and check_pos[1] >= 0 and check_pos[1] < len(warehouse):
        if warehouse[check_pos[1]][check_pos[0]] == ".":
            return check_pos
        if warehouse[check_pos[1]][check_pos[0]] == "#":
            return False
        check_pos = (check_pos[0] + dir[0], check_pos[1] + dir[1])

    return False

def move(pos, dir, free_pos):
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
            if warehouse[y][x] == "O":
                gps += x + 100*y
    return gps

# print("Start")
# print_warehouse(warehouse)
for idx, order in enumerate(orders):
    maybe_move = can_move(robot_pos, dirs[order])
    # print(maybe_move)
    if maybe_move is not False:
        robot_pos, warehouse = move(robot_pos, dirs[order], maybe_move)
    print(f"Order {order}")
    print_warehouse(warehouse)

print(calculate_gps(warehouse))