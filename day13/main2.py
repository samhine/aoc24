from collections import defaultdict

with open("input.txt", "r") as file:
    input = file.read().split("\n\n")
    input = [x.splitlines() for x in input]

def extract_input(input_section):
    d = defaultdict(tuple)
    a_sec = input_section[0].replace("Button A: X+", "").replace(" Y+", "")
    b_sec = input_section[1].replace("Button B: X+", "").replace(" Y+", "")
    t_sec = input_section[2].replace("Prize: X=", "").replace(" Y=", "")

    print(a_sec, b_sec, t_sec)

    return {
        "a": (int(a_sec.split(",")[0]), int(a_sec.split(",")[1])),
        "b": (int(b_sec.split(",")[0]), int(b_sec.split(",")[1])),
        "t": (int(t_sec.split(",")[0]), int(t_sec.split(",")[1]))
    }

def calc_ratio(ax, ay, bx, by, tx, ty):
    # Solve for A, B in the following
    # A(ax) + B(bx) = tx
    # A(ay) + B(by) = ty

    A = (by*tx - ty*bx) / (ax*by - bx*ay)
    B = (tx - ax*A) / bx

    return A, B

input = [extract_input(x) for x in input]
print(input)

tot = 0

for challenge in input:
    found = False
    challenge["t"] = (challenge["t"][0]+10000000000000, challenge["t"][1]+10000000000000)
    ratio = calc_ratio(challenge["a"][0], challenge["a"][1], challenge["b"][0], challenge["b"][1], challenge["t"][0], challenge["t"][1])
    print(ratio)
    if ratio[0] % 1 == 0 and ratio[1] % 1 == 0:
        tot += ratio[1] + 3*ratio[0]

print(tot)