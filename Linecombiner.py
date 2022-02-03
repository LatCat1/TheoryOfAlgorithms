# a line is represented by a (m,b) tuple for the form y=mx+b

def combine(lines):
    # start by sorting the lines
    lines.sort()
    # remove duplicate slopes, keeping the one with a larger y-intercept. 
    # i don't think this is technically needed, but it means that intersect
    # is always safe to call
    i = 0
    while i < len(lines)-1: 
        if lines[i][0] == lines[i+1][0]:
            lines.pop(i)
        else:
            i += 1
    return merge(lines)

# returns the x of where two lines intersect
intersect = lambda a, b: (a[1]-b[1])/(b[0]-a[0])

def merge(lines):
    if len(lines) == 1: # base case
        return lines

    # split into halves based on slope
    half1 = merge(lines[:len(lines)//2])
    half2 = merge(lines[len(lines)//2:])

    # note that eventually, half2 *must* become on top
    # so walk through half1 to find out where it comes on top
    combined = [half1.pop(0)]
    while half1 and intersect(half1[0],combined[-1]) < intersect(half2[0],combined[-1]):
        combined.append(half1.pop(0))
    # ok so we've gotten as far into half1 as we possibly can. now we need to *start* far enough into half2
    while len(half2) > 1 and \
        intersect(half2[0],combined[-1]) >= intersect(half2[1],combined[-1]):
        half2.pop(0) 

    combined.extend(half2)
    return combined


# each is a tuple. index 0 is the test, index 1 is the expected result
tests = [
    (
        [(0,0),(0,1)],
        [(0,1)]
    ),
    (
        [(0,0),(1,1)],
        [(0,0),(1,1)]
    ),
    (
        [(1,2),(3,4),(5,6)],
        [(1,2),(5,6)]
    ),
    (
        [(1,2),(3,4),(5,7)],
        [(1,2),(5,7)]
    ),
    (
        [(-1,-2),(0,0),(1,0)],
        [(-1,-2),(0,0),(1,0)]
    ),
    (
        [(-1,-2),(0,0),(1,4),(5,0)],
        [(-1,-2),(1,4),(5,0)]
    )
]

if __name__ == "__main__":
    errors = 0
    for test,result in tests:
        try:
            assert combine(test) == result
        except AssertionError as e:
            print(f'Failed on {test}: {combine(test)} != {result}')
            errors += 1
    print(f"Score: {len(tests)-errors}/{len(tests)}")
