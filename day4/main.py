import regex as re

with open("input.txt", "r") as file:
    input = file.read().splitlines() 

s = "(XMAS|SAMX)"

def creatediag(array):
    diags = []
    start_points = [(x, 0) for x in range(len(array[0]))] + [(0, x) for x in range(1, len(array))]
    print(start_points)
    print(len(start_points))
    for sx, sy in start_points:
        diag = []
        x = sx
        y = sy
        while x < len(array[0]) and y < len(array) and y >= 0 and x >= 0:
            try:
                diag.append(array[y][x])
            except:
                pass
            x += 1
            y += 1
        diags.append("".join(diag))
    return diags

def creatediag2(array):
    diags = []
    start_points = [(x, 0) for x in range(len(array[0]))] + [(len(array[0])-1, x) for x in range(1, len(array))]
    print(start_points)
    print(len(start_points))
    for sx, sy in start_points:
        diag = []
        x = sx
        y = sy
        while x < len(array[0]) and y < len(array) and y >= 0 and x >= 0:
            try:
                diag.append(array[y][x])
            except:
                pass
            x += -1
            y += 1
        diags.append("".join(diag))
    return diags

horizontal = input
vertical = ["".join(x) for x in zip(*input)]

diags = creatediag(input) + creatediag2(input)

print(sum([len(re.findall(s, x, overlapped=True)) for x in horizontal+vertical+diags]))

final = 0
for y in range(len(input[0])):
    for x in range(len(input)):
        count = 0
        if x>0 and y>0 and y+1<len(input[0]) and x+1<len(input) and input[x][y] == "A":
            if (input[x-1][y-1] == "M" and input[x+1][y+1] == "S") or (input[x-1][y-1] == "S" and input[x+1][y+1] == "M"):
                count += 1
            if (input[x-1][y+1] == "M" and input[x+1][y-1] == "S") or (input[x-1][y+1] == "S" and input[x+1][y-1] == "M"):
                count += 1
        if count == 2:
            final += 1
        
print(final)