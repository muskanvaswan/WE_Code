"""
 1   
 2  3
 4  5  6
 7  8  9  10
11 12 13
"""
def line(count, width, number):
    result = ""
    for i in range(width):
        if not count <= number:
            break
        result += str(count).rjust(4)
        count += 1
    return result, count

def pattern(number):
    pattern_lines = []
    count, width = 1, 1
    while count <= number:
        curr_line, count = line(count, width, number)
        pattern_lines.append(curr_line)
        width += 1
    return pattern_lines

def formatted_pattern(pattern):
    return "\n".join(pattern)

print(formatted_pattern(pattern(16)))
