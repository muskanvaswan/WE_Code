"""
1
2 4
3 6  9
4 8 12 16
"""
def line(width: int, line_len: int) -> str:
    return f"{str(width).rjust(line_len)}" * width

def pattern(height: int) -> [str]:
    line_len = len(str(height)) + 1
    return [line(row, line_len) for row in range(1, height + 1)]

def formatted_pattern(height: int) -> str:
    return "\n".join(pattern(height))

# print(pattern(5))
print(formatted_pattern(int(input("height: "))))

# [ str(i) for i in range(1,  5)]
# ['1', '2', '3', '4']
