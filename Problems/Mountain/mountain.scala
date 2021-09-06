def assignSign(a: Int, b: Int): Int = {
  if (a>b)
    return -1
  else if (a < b)
    return 1
  else
    return 0
}

// return -1 for decreasing and +1 for increasing
val signNum: Array[Int] => Array[Int] = (sequence) =>  (sequence zip sequence.tail).map({ case (x, y) => assignSign(x, y)})

// [-1, -1, 0, 1]
//[(-1, 0), (0, 1)]
// returns a list of all the distinct changes
var switches = (sequence: Array[Int]) => (sequence zip sequence.tail).filter(switch => switch._1 != switch._2)

def isMountain(sequence: Array[Int]): Boolean = {
  val joints = switches(signNum(sequence))
  return (joints(0) == (1, -1)) && (joints.length == 1)
}


println(isMountain(Array(1, 2, 3, 4, 3, 2,1)))
