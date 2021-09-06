import itertools

def euler_problem1(inp: int)  -> int :
    multiples_3_and_5 = set(itertools.chain(range(3, inp, 3), range(5, inp, 5)))
    return sum(multiples_3_and_5)

print(euler_problem1(1000))
