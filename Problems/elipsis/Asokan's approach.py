'''Input -> A string; heading for a story 
Output -> A potentially shorter string to be used in ToCs etc. Depending on where ToC is, can be either 
          25 chars long or 10 chars long. Longer headings will be indicated by truncating and adding n 
          ellipses. The final length, including the ellipsis is expected to be written 25 or 10. '''

PADDING = "..."
OFFSET = len(PADDING)
LONG = 25
SHORT = 10 

def add_padding(s: str) -> str:
    return s + PADDING

def adjust_size(s: str, new_size: int) -> str:
    return s[:(new_size - OFFSET)]

def get_limit(long: bool) -> int:
    return LONG if long else SHORT

def ellipsised_heading(heading: str, long: bool) -> str:
    limit = get_limit(long)
    if len(heading) <= limit:
        return heading
    return add_padding(adjust_size(heading, limit))
print(ellipsised_heading("Let us perform this task together", True))
print(ellipsised_heading("Let us perform this task together", False))
