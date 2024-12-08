with open('input.txt', 'r') as file:
    data = file.readlines()

col1 = []
col2 = []

for line in data:
    line = line.split("   ")
    col1.append(int(line[0]))
    col2.append(int(line[1]))

col1 = sorted(col1)
col2 = sorted(col2)

# PART 1
totdist = 0
for i, x in enumerate(col1):
    dist = abs(col1[i] - col2[i])
    totdist += dist

print(totdist)

# PART 2
similarity = 0
for i, x in enumerate(col1):
    similarity += col1[i] * col2.count(col1[i])

print(similarity)