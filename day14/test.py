width = 9

# ...0 0...
# ..0. .0..
# .0.. ..0.
# ..0. .0..
# ...0 0...


robots = [
    {"p":(3,0)},
    {"p":(5,0)},
    {"p":(2,1)},
    {"p":(6,1)},
    {"p":(1,2)},
    {"p":(7,2)},
    {"p":(2,3)},
    {"p":(6,3)},
    {"p":(3,4)},
    {"p":(5,4)},
    {"p":(4,5)},
    {"p":(4,6)}

]

positions = [x["p"] for x in robots]

symmetrical = True
for each in robots:
    # If for each point (< width//2), there exists another point flipped across width//2 (on the same y) then we have a match
    print(each["p"][0], width-each["p"][0])

    print(each)
    print((width-each["p"][0], each["p"][1]))
    if each["p"][0] >= width//2:
        continue
    elif each["p"][0] < width//2 and (width-each["p"][0]-1, each["p"][1]) in positions:
        continue
    else:
        print("Match not found for ", each)
        symmetrical = False
        break

print(symmetrical)