def printMap(cipher: Map[Char, Char]): Unit = {
  for ((key, value) <- cipher) {
    println(s"$key -> $value")
  }
}

def generateCipher(): Map[Char, Char] = {
  var cipher = Map[Char, Char]()
  for(alphabet <- 'a' to 'm') {
    cipher = cipher + (alphabet -> (alphabet + 13).toChar)
  }
  // inverting map
  cipher = cipher ++ cipher.map(_.swap)

  return cipher
}

def matchCase(matchWith: Char, matchThis: Char): Char = {
  return (if (matchWith.isUpper) matchThis.toUpper else matchThis.toLower)
}


def decipher(message: String): String = {
  var deciphered = ""
  var cipher = generateCipher()
  for (character <- message)
    deciphered += matchCase(character, cipher.getOrElse(character.toLower, character))
  return deciphered


println(decipher("Abc"))
