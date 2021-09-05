# Si = 1 + revrse(invert(Si-1)) for i > 1
def reverse(string: str) -> str:
    return string[::-1]

def invert_bit(bit: str) -> str:
    return "0" if bit == "1" else "1"

def invert(binary_string: str) -> str:
    return "".join([invert_bit(bit) for bit in binary_string])

def sequence(i: int) -> str:
    return (sequence(i - 1) + "1" + reverse(invert(sequence(i - 1)))) if i > 1 else "0"

def bit_in_sequence(bit_string: str, bit_place: int) -> str:
    return bit_string[bit_place - 1]

print(bit_in_sequence(sequence(0), 1))
print(bit_in_sequence(sequence(4), 11))
print(bit_in_sequence(sequence(2), 3))
