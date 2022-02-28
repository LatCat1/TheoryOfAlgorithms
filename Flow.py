from ast import Num

Graph = dict[str, dict[str,Num]]

G1: Graph = {
    's':{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1},
    'a':{'h':1,'i':1,'j':1},
    'b':{'g':1,'k':1},
    'c':{'h':1,'i':1,'j':1,'l':1},
    'd':{'k':1,'l':1},
    'e':{'g':1,'k':1,'l':1},
    'f':{'g':1,'l':1},
    'g':{'t':1},
    'h':{'t':1},
    'i':{'t':1},
    'j':{'t':1},
    'k':{'t':1},
    'l':{'t':1}
}

G2: Graph = {
    's':{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1},
    'a':{'g':1,'k':1,'l':1},
    'b':{'g':1,'h':1,'i':1},
    'c':{'g':1,'j':1},
    'd':{'g':1,'j':1},
    'e':{'h':1,'i':1,'l':1},
    'f':{'j':1,'k':1},
    'g':{'t':1},
    'h':{'t':1},
    'i':{'t':1},
    'j':{'t':1},
    'k':{'t':1},
    'l':{'t':1}
}

def eval_cut(L: set[str], graph: Graph, maxval=1000):
    assert 's' in L
    if not is_connected(L, graph):
        return maxval
    s = 0
    for f in L:
        for target in graph[f]:
            if target not in L:
                s += graph[f][target]
    return s

def is_connected(S: set[str], graph: Graph):
    assert 's' in S
    founds = set()
    queue = ['s']
    while queue != []:
        founds.add(queue[0])
        x = set(graph[queue.pop(0)]).intersection(S)
        queue.extend(list(x))
        founds = founds.union(x)

    return len(founds) == len(S)

def powerset(p: list):
    for i in range(2**len(p)):
        x = p.copy()
        y = []
        while i > 0:
            if i%2 == 1:
                y.append(x[0])
            x.pop(0)
            i //= 2
        yield y

graph = G2

m, r = min(((eval_cut(set(c).union({'s'}),graph), c + ['s']) for c in powerset(list("abcdefghijkl"))),
    key = lambda x: x[0]*1000 + len(x[1])) # key lambda is to prioritize smaller L cuts

r = list(r)
r.sort()
print(f'L = {r} got a min score of {m}')