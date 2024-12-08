import copy

with open('input.txt', 'r') as file:
    data = file.readlines()

def findifsafe(level):
    increasing = level[0] < level[1]
    tolerated = False
    for ii, x in enumerate(level):
        if ii == len(level)-1:
            continue
        
        if abs(x-level[ii+1]) <= 3 and increasing == (x < level[ii+1]) and (x-level[ii+1]) !=0:
            continue
        else:
            return False
    
    return True
        

safe = 0
for i in data:
    level = i.split(" ")
    level = [int(x) for x in level]
    
    if findifsafe(level):
        safe += 1
    else:
        for ii, x in enumerate(level):
            test = copy.deepcopy(level)
            test.pop(ii)
            if findifsafe(test):
                safe += 1
                break

print(safe)