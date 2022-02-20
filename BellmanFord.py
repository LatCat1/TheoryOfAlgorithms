from ast import Num

Graph = dict[str, dict[str,Num]]

m: Graph = {
    's': {'a':6,'d':3,'g':3},
    'a': {'b':2},
    'b': {'c':2,'d':-6,'e':6},
    'c': {'t':7},
    'd': {'a':5,'e':11,'g':-1},
    'e': {'f':-6},
    'f': {'b':2,'c':-2,'h':-1,'i':9,'t':6},
    'g': {'h':3},
    'h': {'d':-1,'e':8,'i':10},
    'i': {'t':-3},
    't': {}
}

def display(iter, dists):
    out = f""
    for n in dists:
        out += f"${n}$ costs {dists[n]}, "
    return out[:-2]

def bellman_ford(source: str, graph: Graph, disp: bool = False, 
    default_max: Num = 10000) -> dict[str, Num]:
    
    dist = {source: 0}
    view = []
    for k in range(1,len(graph)):
        copy = {}
        temp_look = [d for d in dist.keys()]
        for u in temp_look:
            for v in graph[u]:
                copy[v] = min(dist.get(v,default_max),  dist.get(u,default_max) + graph[u][v])
        for i in copy:
            dist[i] = copy[i]

        if disp: view.append(display(k, dist))

    if disp:
        while view[-1] == view[-2]:
            view.pop()
        for i in range(len(view)):
            print(f'For walks from $s$ of at most $k={i+1}$ edges: {view[i]}')

    return dist

(bellman_ford('s', m, disp=True))