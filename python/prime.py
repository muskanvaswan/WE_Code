def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int((n**0.5)+1), 2):
      if n%i == 0:
        return False
    return True

# Driver Code
checking_for = int(input("Enter number:"))
if is_prime(checking_for):
    print(f"The number is prime")
else:
    print(f"The number is not prime")
