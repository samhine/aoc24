from functools import cache

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    patterns = tuple(input[0].split(", "))
    displays = input[2:]

print(patterns)
print(displays)

@cache
def check_pattern_possible(display, patterns):
    if display in patterns:
        return True
    possible = False
    for pattern in patterns:
        if display.startswith(pattern):
            if check_pattern_possible(display[len(pattern):], patterns):
                possible = True
                break
    return possible

@cache
def count_possible_patterns(display, patterns):
    possible = 0
    if display in patterns:
        possible += 1
    for pattern in patterns:
        if display.startswith(pattern):
            possible += count_possible_patterns(display[len(pattern):], patterns)
    return possible

possible = 0
for display in displays:
    if check_pattern_possible(display, patterns):
        possible += 1

print(possible)

count = 0
for display in displays:
    count += count_possible_patterns(display, patterns)

print(count)