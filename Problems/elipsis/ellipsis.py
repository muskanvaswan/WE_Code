ELIPSIS = '...'
OFFSET = len(ELIPSIS)

LENGTHS = {
    True: 25,
    False: 10
}

def ellipsised_heading(heading: str, long = False) -> str:
    return  add_elipsis(trunc_heading(heading, long), long)

def trunc_heading(heading: str, long: bool) -> str:
    return heading[:LENGTHS[long] - OFFSET] if len(heading) > LENGTHS[long] else heading

def add_elipsis(heading: str, long: bool) -> str:
    return heading + ELIPSIS if len(heading) == LENGTHS[long] - OFFSET else heading


# Example
print(ellipsised_heading("Let us understand Typography"))
print(ellipsised_heading("Let us understand Typography", long=True))
