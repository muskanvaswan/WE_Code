def removeAscending(sequence: Array[Int]) : Array[Int] = {
  return (sequence zip sequence.tail).filter(switch => switch._1 >= switch._2).map({case (x, y) => x})
}

println(removeAscending(Array(1, 2, 3, 4, 5, 4, 3, 2, 1)))
