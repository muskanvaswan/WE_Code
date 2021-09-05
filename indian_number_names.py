BEFORE20 = {
    0: '',
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten',
    11:'Eleven',
    12:'Twelve',
    13:'Thirteen',
    14:'Fourteen',
    15:'Fifteen',
    16:'Sixteen',
    17:'seventeen',
    18:'Eighteen',
    19:'Nineteen'
}
TENS = {
    1:'One',
    2:'Twenty',
    3:'Thirty',
    4:'Fourty',
    5:'Fifty',
    6:'Sixty',
    7:'Seventy',
    8:'Eighty',
    9:'Ninety'
}
PLACES = {
    1: '',
    10: TENS,
    100: 'Hundred',
    1000: 'Thousand',
    100000: 'Lakh',
    10000000: 'Crore'
}

def name_for_number(number):
    if number < 20:
        return BEFORE20[number]
    else:
        return TENS[int(number/10)] + ' ' + BEFORE20[number%10]

def place_value(number):
    val = 10**(number_of_digits(number)-1)
    if val not in PLACES.keys():
        return val/10
    return val

def name_for_start_of_number(number, place_val):
    result = ''

    if place_val <= 10:
        result += name_for_number(number)
    else:
        name_for = int(number/place_val)
        result += name_for_number(name_for)
        result += ' ' + PLACES[place_val]

    return result

def number_of_digits(number):
    return len(str(int(number)))

def number_name(number, string=''):
    if number == 0:
        return string
    place_val = place_value(number)

    if place_val == 10:
        if string == '':
            string += name_for_start_of_number(number, place_val) + ' '
        else:
            string += 'and ' + name_for_start_of_number(number, place_val)
        return string

    string += name_for_start_of_number(number, place_val) + ' '
    return number_name(number%place_val, string)

print(number_name(113))
