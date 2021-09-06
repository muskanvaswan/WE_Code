def getDigits(n: Int): (Int, IndexedSeq[Int]) = {
  var nString = n.toString
  return (nString.length, nString.map(_.asDigit))
}

def checkArmstrong(n: Int): Boolean = {
  var sumOfCubes = 0
  val (noOfDigits, digits) = getDigits(n)
  for (digit <- digits)
    sumOfPowers = sumOfPowers + scala.math.pow(digit, noOfDigits).toInt
  return (sumOfPowers == n)
}

def armstrong(start: Int, end: Int): Int = {
  for (number <- start until end) {
    if (checkArmstrong(number))
      return number
  }
  return -1
}

println(armstrong(200, 500))
