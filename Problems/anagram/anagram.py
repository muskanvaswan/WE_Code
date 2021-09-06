def check_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def anagram_group(word, words):
    return [word2 for word2 in words if check_anagram(word, word2)] + [word]

def anagram_groups(words):
    anagram_result = []

    while len(words) != 0:
        word = words.pop()
        anagrams = anagram_group(word, words)
        words -= set(anagrams)

        if len(anagrams) > 1:
            anagram_result.append(anagrams)

    return anagram_result

words = {'could', 'cloud', 'areas', 'arena', 'artsy', 'grips', 'hello', 'parts', 'prigs', 'strap', 'traps'}
print(anagram_groups(words))
