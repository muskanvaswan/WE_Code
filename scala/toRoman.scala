import scala.collection.mutable.TreeSet

def closestBase(n: Int): Int = {
  var bases = TreeSet.empty(Ordering.fromLessThan[Int](_ < _))
  bases += (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 900, 1000)
  if (bases.contains(n))
    return bases.toIndexedSeq(bases.toIndexedSeq.indexOf(n))
  bases += n
  if (n == 1)
    return 1
  return bases.toIndexedSeq(bases.toIndexedSeq.indexOf(n) - 1)
}

def getSymbol(n: Int): String = n match {
    case 1 => "I"
    case 4 => "IV"
    case 5 => "V"
    case 9 => "IX"
    case 10 => "X"
    case 40 => "XL"
    case 50 => "L"
    case 90 => "XC"
    case 100 => "C"
    case 400 => "CD"
    case 500 => "D"
    case 900  => "CM"
    case 1000 => "M"
}

def makeRoman(n: Int, output: String = ""): String = {
  if (n == 0) {
    return output
  } else {
    var base = closestBase(n)
    return makeRoman(n % base , output ++ (getSymbol(base) * (n/base)))
  }
}

def toRoman(number: Int): String = {
  return makeRoman(number)
}

// Driver Code
println(toRoman(args(0).toInt))
