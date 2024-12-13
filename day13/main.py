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

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

input = [extract_input(x) for x in input]
print(input)

tot = 0

for challenge in input:
    found = False
    for b_attempt in range(101,0,-1):
        if found:
            break
        for a_attempt in range(1,101):
            if found:
                break
            b_mult = b_attempt
            a_mult = a_attempt

            a = (challenge["a"][0] * a_mult, challenge["a"][1] * a_mult)
            b = (challenge["b"][0] * b_mult, challenge["b"][1] * b_mult)
            t = challenge["t"]

            if a[0] + b[0] == t[0] and a[1] + b[1] == t[1]:
                tot += b_attempt + 3*a_attempt
                target_prime_factors = (prime_factors(challenge["t"][0]),prime_factors(challenge["t"][1]))
                a_prime_factors = (prime_factors(challenge["a"][0]),prime_factors(challenge["a"][1]))
                b_prime_factors = (prime_factors(challenge["b"][0]),prime_factors(challenge["b"][1]))


                print(target_prime_factors, a_prime_factors, b_prime_factors)
                print(prime_factors(a_attempt), prime_factors(b_attempt))
                found = True

print(tot)