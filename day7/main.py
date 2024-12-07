import itertools

with open("input.txt", "r") as file:
    input = file.read().splitlines()
    input = [
        {
            "op": x.split(": ")[0],
            "arg": x.split(": ")[1].split(" ")
        } for x in input
    ]

map_op = {
    "0": "*",
    "1": "+",
    "2": "||"
}
def calculate(nums, ops):
    insert = 1
    calc = [x for x in nums]
    for k in ops:
        calc.insert(insert, map_op[k])
        insert += 2

    tot = int(calc[0])
    for i in range(1, len(calc), 2):
        if calc[i] == "+":
            tot += int(calc[i+1])
        elif calc[i] == "*":
            tot *= int(calc[i+1])
        elif calc[i] == "||":
            tot = int(str(tot) + str(calc[i+1]))
    return tot

part1 = "01"
part2 = "012"

results = []
for calc in input:
    positions = len(calc["arg"])-1
    permutations = ["".join(seq) for seq in itertools.product(part2, repeat=positions)]
    for permutation in permutations:
        result = calculate(calc["arg"], permutation)
        if result == int(calc["op"]):
            results.append(result)
            break

print(sum(results))
