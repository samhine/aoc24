from collections import defaultdict

with open("input.txt", "r") as file:
    input = file.read().splitlines()

with open("instruc.txt", "r") as file:
    instruc = file.read().splitlines()

after = defaultdict(list)
before = defaultdict(list)

for r in input:
    target, value = r.split("|")
    after[target].append(value)
    before[value].append(target)

def valid(current, all):
    idx = all.index(current)
    # check backwards
    for i in range(idx-1, -1, -1):
        if all[i] in after[current]:
            return False
    # check forwards
    for i in range(idx+1, len(all)):
        if all[i] in before[current]:
            return False
    return True

tot = 0
invalid = []
for i in instruc:
    j = i.split(",")
    v = True
    for ii in j:
        if valid(ii, j):
            continue
        else:
            v = False
            invalid.append(j)
            break
    if v:
        tot += int(j[len(j)//2])

print(tot)

from functools import cmp_to_key

def sort(x,y):
    if x in after[y]:
        return -1
    if y in after[x]:
        return 1
    return 0

tot = 0
for i in invalid:
    s = sorted(i, key=cmp_to_key(sort))
    tot += int(s[len(s)//2])

print(tot)