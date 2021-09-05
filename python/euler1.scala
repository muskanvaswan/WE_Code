def eulerProblem1(input: Int): Int = {
  var current_sum = 0
  for (x <- 1 until input){
    if (x%3 == 0 || x%5 == 0){
      current_sum = current_sum + x
    }
  }
  return current_sum
}
println(eulerProblem1(1000))
