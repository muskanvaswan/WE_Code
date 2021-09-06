import itertools

# summation n = n(n+1)/2
# if m is the multiple
# new_n = (n-1)//m
# then summation for new_n = m (summation of new n)

summation = lambda n, m: m * ((n - 1) // m) * ((n - 1) // m + 1) // 2


def euler_problem1(inp: int)  -> int :
    # removing common multiples between 3 and 5
    divisible_3_or_5 = summation(inp, 3) + summation(inp, 5) - summation(inp, 15)
    return result

print(euler_problem1(10))
