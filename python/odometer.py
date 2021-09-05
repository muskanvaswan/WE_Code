#  rule 1: no zeroes
# rule 2: no ascending

def is_valid(num: int) -> bool:
    digits_of_num = break_into_digits(num)

    if 0 in digits_of_num:
        return False

    if not digits_of_num == sorted(digits_of_num):
        return False

    if not len(digits_of_num) == len(set(digits_of_num)):
        return False

    return True

def break_into_digits(num: int) -> [int]:
    return [int(n) for n in str(num)]

 

def ending(size: int) -> int:
    return int(''.join(str(i) for i in range(9, 9 - digits + 1, -1)))

def next_reading(num: int) -> int:
    num += 1
    while not is_valid(num):
        num += 1
    return num

def odometer(size: int):
    reading = starting(size)
    last_reading = ending(size)

    while True:
        print(reading)
        reading = next_reading(reading)
        if reading >= last_reading:
            reading = starting

print(next_reading(123))
print(odometer(3))
