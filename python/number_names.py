import sys

BEFORE20 = [ '','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','seventeen','Eighteen','Nineteen']
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

# Deciding the number system
if sys.argv[1] == 'western':
    PLACES = {
        1: '',
        100: 'Hundred',
        1000: 'Thousand',
        1000000: 'Million',
        1000000000: 'Crore'
    }
else:
    PLACES = {
        1: '',
        100: 'Hundred',
        1000: 'Thousand',
        100000: 'Lakh',
        10000000: 'Crore'
    }

def name_for_number(number):
    if number < 20:
        return BEFORE20[number]
    elif number < 100:
        return TENS[int(number/10)] + ' ' + BEFORE20[number%10]
    else:
        return number_name(number)

def place_value(number):
    val = 10**(number_of_digits(number)-1)
    while val not in PLACES.keys():
        val /= 10
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

def number_name(number, name=''):
    if number == 0:
        return name
    place_val = place_value(number)

    # Handling for Tens values
    if place_val == 10:

        # Handling the placement of 'and'
        if name == '':
            name += name_for_start_of_number(number, place_val) + ' '
        else:
            name += 'and ' + name_for_start_of_number(number, place_val)
        return name

    name += name_for_start_of_number(number, place_val) + ' '
    return number_name(number%place_val, name)

print(number_name(int(sys.argv[2])))
