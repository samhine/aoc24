import itertools
from collections import defaultdict

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    available = input[0].split(", ")
    patterns = input[2:]

print(available)
print(patterns)

# Go through pattern with pointers, if we find match between our pointers, save it, and continue until pointers have scanned entire string
# Then we go through our saved matches, and repeat the process
# If our saved matches == the string 

def find_matches(string, current_matches, completed=[]):
    #print(string, current_matches)
    next_matches = []
    accounted = []
    for match in current_matches:
        coagulated = ''.join(match)
        if string == coagulated:
            completed.append(match)
            continue
        
        # Align pointers to next character after match in string
        idx = [idx for idx, val in enumerate(string) if string[:idx] == coagulated][0]
        lp = idx
        rp = idx+1

        while rp <= len(string):
            if string[lp:rp] in available:
                #print("Found", string[lp:rp])
                new_match = match.copy()
                new_match.append(string[lp:rp])
                new_coagulated = ''.join(new_match)
                if new_coagulated not in accounted: # Do not append duplicates
                    accounted.append(new_coagulated)
                    next_matches.append(new_match)
                
            rp += 1

    if len(next_matches) == 0:
        print(completed)
        return len(completed)
    
    return find_matches(string, next_matches, completed)

found = 0
for pattern in patterns:
    print(pattern)
    found += find_matches(pattern, [[""]], [])

print(found)

