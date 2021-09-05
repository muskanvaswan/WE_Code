# if any part of 789 is found in the number then remove it and pick up the first nuber before it
# ['789', '89', '9']

# 6789
def get_end_list(number_of_digits: int) -> [int]:
    #gives back something like ['789', '89', '9']
    return []

def find_ending_index_in_number(str_number: str, no_of_digits) -> int:
    end_list = get_end_list()
    idx = -1
    for i, n in enumerate(str_number):
        if str_number[-i] == end_list[-i]:


def next_reading(number: int, no_of_digits: int) -> int:
    str_number = str(number)
    ending_position = find_endings_in_number(str_number, no_of_digits)

    if ending_position != -1:
        return construct(str_number[ending_position - 1:], no_of_digits)

    else:
        return number + 1

def construct_reading(starting_digit: int, no_of_digits: int) -> int:

    # 289 -> pick up 2 and make 345 which is 2+1, 2+2 2+3
    return 0
