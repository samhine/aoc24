import itertools

with open("input.txt", "r") as f:
    input = f.read().strip()

print(input)
formatted = []

def checksum(something):
    v = 0
    for idx, id in enumerate(something):
        if id == ".":
            continue
        v += idx*int(id)
    return v

def chunkify(something):
    return [list(g) for _, g in itertools.groupby(something)]    

def flatten(something):
    return [ii for i in something for ii in i]

for idx, char in enumerate(input):
    if idx % 2 == 0:
        # we need to treat ids as individual objects.. 
        # ids 10 or higher will bork
        formatted.extend([str(idx//2)] * int(char))
    else:
        formatted += "." * int(char)

part1 = False

if part1:
    lp = 0
    rp = len(formatted) - 1
    while lp < rp:
        if formatted[lp] == "." and formatted[rp] != ".":
            formatted[lp] = formatted[rp]
            formatted[rp] = "."
            lp += 1
            rp -= 1
        elif formatted[lp] == "." and formatted[rp] == ".":
            rp -= 1
        else:
            lp += 1
    
    print(formatted)
    print(checksum(formatted))
else:
    chunked = chunkify(formatted)

    lp = 0
    rp = len(chunked) - 1
    while rp > 0:
        # print(chunked)
        if lp == rp:
            rp -= 1
            lp = 0
            continue

        lp_char = chunked[lp][0]
        rp_char = chunked[rp][0]
        if rp_char == ".":
            rp -= 1
            lp = 0
            continue

        # print(lp_char, rp_char)

        if lp_char == "." and rp_char != ".":
            # print("lengths", len(chunked[lp]), len(chunked[rp]))
            if len(chunked[lp]) >= len(chunked[rp]):
                # print("swap!")
                size_diff = len(chunked[lp]) - len(chunked[rp])
                chunked[lp] = [rp_char] * len(chunked[rp])
                if size_diff:
                    chunked[lp] += ["."] * size_diff
                chunked[rp] = ["."] * len(chunked[rp])
                chunked = chunkify(flatten(chunked))

                rp -= 1
                lp = 0

        lp += 1
    print(chunked)
    # print(''.join([ii for i in chunked for ii in i]))
    # print([ii for i in chunked for ii in i])
    # print(flatten(chunked))
    print(checksum(flatten(chunked)))
