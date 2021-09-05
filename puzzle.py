import string

SENTENCE_FORM = "This sentence has A 0's, B 1's, C 2's, D 3's, E 4's, F 5's, G 6's, H 7's, I 8's, and J 9's"
SENTENCE_BLANKS = map(SENTENCE_FORM.split().index, string.ascii_uppercase[:10])

def extract_from_sentence(sentence: str) -> [int]:
    return [int(word) for idx, word in enumerate(sentence.split()) if idx in SENTENCE_BLANKS]

def find_appearances(sentence: str, number: int) -> int:
    return sentence.count(str(number))

def check_validity(value: int, sentence: str, number: int) -> bool:
    return  value == find_appearances(sentence, number)

def check_sentence(sentence: str) -> bool:
    for idx, value in enumerate(extract_from_sentence(sentence)):
        if not check_validity(value, sentence, idx):
            return False
    return True

sentence = "This sentence has 1 0's, 7 1's, 3 2's, 2 3's, 1 4's, 1 5's, 1 6's, 2 7's, 1 8's, and 1 9's"
print(check_sentence(sentence))
