def pattern(number):
    result = ""
    count, line_num = 1, 1

    while count <= number:
        result += str(count).rjust(4)

        if count == line_num * (line_num + 1) / 2:
            result += "\n"
            line_num += 1

        count += 1

    result += "\n*"

    return result

print(pattern(13))
