def outputForX(x: Int, parameters: Array[(String, (Int) => Boolean)]): String = {
  var output = ""

  for((result, checkFunc) <- parameters) {
    if (checkFunc(x)) {
      output += result
    }
  }

  if (output.length == 0)
    output = x.toString()

  output += "\n"

  return output
}

def fizzbuzz(n: Int, parameters: Array[(String, (Int) => Boolean)]): String = {
  var result = ""
  for(x <- 1 until n) {
    result += outputForX(x, parameters)
  }
  return result
}

// Driver code
print(fizzbuzz(args(0).toInt, Array(
  ("Fizz", (x: Int) => { x%3 == 0 }),
  ("Buzz", (x: Int) => { x%5 == 0 }),
  ("Zass", (x: Int) => { x%7 == 0}),
)))
