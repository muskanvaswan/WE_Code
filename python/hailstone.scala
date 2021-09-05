import scala.io.StdIn.readInt

def nextElement(previous: Int): Int = {
  // helper function to find next element
  if (previous % 2 == 0)
    return previous / 2
  else
    return (previous * 3) + 1
}

def hailstoneSequence(start: Int): Array[Int] = {
  var sequence = Array(start, 0, 0)
  var collatzTerminator = Array(4, 2, 1)

  sequence(1) = nextElement(start)
  sequence(2) = nextElement(sequence(1))

  while(!seq.endsWith(collatzTerminator)) {
    lastThreeNumbers = lastThreeNumbers :+ nextElement(sequence.last)
  }

  return sequence
}

// Driver Code
print("Enter the first element: ")
var inp = readInt()
print("Here is your sequence: ")
for(x <- hailstoneSequence(inp).toIterable){
  printf("%d ", x)
}
println(" ")
