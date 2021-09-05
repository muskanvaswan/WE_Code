def take_case():
    case = {
        's': 0,
        'browsers': [],
        'q': 0,
        'queries': []
    }
    case['s'] = int(input())
    case['browsers'] = [input() for i in range(case['s'])]
    case['q'] = int(input())
    case['queries'] = [input() for i in range(case['q'])]

    return case

N = int(input())
cases = [take_case() for i in range(N)]

def switch_to(browsers, queries):
    count = len(queries)
    switching = ''
    queries = tuple(queries)
    for browser in browsers:
        occourance = queries.count(browser)
        # print(occourance, browser)
        if occourance < count:
            count = occourance
            switching = browser
    return switching

def min_switches(browsers, queries):
    searcher = switch_to(browsers, queries)
    count = 0
    for idx, query in enumerate(queries):
        if searcher == query:
            searcher = switch_to([br for br in browsers if br != searcher], queries[idx:])
            count += 1
        # print("    " + searcher)
    return count

switches = 0
# print(cases)
for index, case in enumerate(cases):
    # print(case)
    switches = min_switches(case['browsers'], case['queries'])
    print(f"Case #{index+1}: {switches}")
print()
