import sys
from typing import List

def output_for_x(x: int, parameters: List) -> str:
  output = ""
  for (result, checkFunc) in parameters:
    if checkFunc(x):
      output += result
  if len(output) == 0:
    output = str(x)
  output += "\n"
  return output


def fizzbuzz(n: int, parameters: List) -> str:
  result = ""
  for x in range(1, n):
    result += output_for_x(x, parameters)
  return result

# Driver code
print(fizzbuzz(int(sys.argv[1]), [
  ("Fizz", lambda x: x%3 == 0 ),
  ("Buzz", lambda x: x%5 == 0 ),
  #("Zass", lambda x: x%7 == 0 ),
]), end="")
