# a line is represented by a (m,b) tuple for the form y=mx+b
Line = tuple[float, float]

def combine(lines: list[Line]) -> list[Line]:
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
def intersect(a: Line, b: Line) -> float:
    return (a[1]-b[1])/(b[0]-a[0])

def calc(line: Line, point: float) -> float:
    return line[0]*point+line[1]

def merge(lines: list[Line]) -> list[Line]:
    if len(lines) == 1: # base case
        return lines
    #print('Merging', lines)
    # split into halves based on slope
    half1 = merge(lines[:len(lines)//2])
    half2 = merge(lines[len(lines)//2:])

    # disqualify as many from the *end* of half1 as possible
    # TODO: add guards to avoid index out of bounds
    changed = 1
    while changed:
        changed = 0
        #print('The current state is', half1, half2)
        # check that len(half1)>1 because the line with the smallest slope
        # will never be removed
        # what the second clause is finding where the line before the last in h1 and
        # the first in h2 intersect. it then gets the y-value for both. 
        # if h1[-2](intersect) >= h1[-1](intersect) <=> h2[0](intersect) >= h1[-1](intersect)
        # then max(h1[-2],h1[0f]) >= h1[-1] for all x, so get rid of h1[-1]
        while len(half1) > 1 and \
            calc(half1[-2], intersect(half1[-2], half2[0])) >= \
                calc(half1[-1], intersect(half1[-2], half2[0])):
            changed = 1
            #print(f'Yeeting {half1[-1]}')
            half1.pop(-1)

        # now disqualify as many from the *start* of half2 as possible
        # guards against len(half2)==1 because the largest slope will always be kept
        # as before, this checks if the intersection point of the lines 'before' and 'after'
        # a line
        # if h2[0](intersect) <= h1[-1](intersect) <=> h2[0] <= h2[1](intersect) then equivalently
        # h2[0] <= max(h1[-1],h2[1]) for all x, so get rid of h2[0]
        while len(half2) > 1 and \
            calc(half1[-1], intersect(half1[-1], half2[1])) >= \
                calc(half2[0], intersect(half1[-1], half2[1])):
            changed = 1
            #print(f'Yeeting {half2[0]}')
            half2.pop(0)

    #print('Final state is', half1+half2)
    return half1 + half2

# each is a tuple. index 0 is the test, index 1 is the expected result
tests: list[tuple[list[Line],list[Line]]] = [
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
    ),
    (
        [(-1,2),(-0.5,1.25),(0,0),(1,0)],
        [(-1,2),(1,0)]
    ),
    (
        [(-1,-2),(-0.5,-1.25),(0,0),(1,0)],
        [(-1,-2),(0,0),(1,0)]
    ),
    (
        [(1,-2),(0.5,-1.25),(0,0),(-1,0)],
        [(-1,0),(0,0),(1,-2)]
    ),
    (
        [(1,2),(0.5,1.25),(0,0),(-1,0)],
        [(-1,0),(1,2)]
    )
]

if __name__ == "__main__":
    errors = 0
    runs = 0
    for test,result in tests:
        runs += 1
        r = combine(test)
        try:
            assert r == result
        except AssertionError as e:
            print(f'Failed on {test}: {r} != {result}')
            errors += 1
    print(f"Score: {runs-errors}/{runs}")
