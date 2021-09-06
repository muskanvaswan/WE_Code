import itertools


def prime_factors(n: int) -> [int]:

    if n < 2:
        return prime_factors

    prime_factors = []

    for factor in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % factor == 0:
            n //= factor # integer division
            prime_factors.append(factor)
    return prime_factors

# Driver code
finding_for = int(input("Enter number: "))
print(prime_factors(finding_for))
