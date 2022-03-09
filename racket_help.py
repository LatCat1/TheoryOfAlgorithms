def spanning_forest(graph): # graph : graph, -> spanning_forest
    pass

g = [
   (5, 'A',[1,3])    ,#;; A -> B; D
   (2, 'B',[3])      ,#;; B -> D
   (8, 'C',[1, 4, 5])  ,#;; C -> B; E; F
   ( 0, 'D',[4, 6, 7,])  ,#;; D -> E; G; H
   ( 3, 'E',[1, 6])    ,#;; E -> B; G
   ( 7, 'F',[5])      ,#;; F -> F
   ( 6, 'G',[])       ,#;; G ->
   ( 1, 'H',[])     ,#;; H ->
]


def foldr(func, val, l):
    if l == []:
        return val
    return foldr(func, func(val, l[0]), l[1:])

# graph A -> (list(gnode A), forest A) -> int -> (list(gnode A), forest A)
def helper(graph, pair, node):
    if node not in pair[0]:
        new_visited, tree = accum(graph, pair[0], node)  #
        return (new_visited, pair[1] + [(graph[node][1], tree)])
    return pair

# graph A -> list(gnode A) -> int -> (set[gnode A], tree A)
def accum(graph, visited, node):   # node : visited # add the vector-ref of node instead
    return foldr(lambda a,b: helper(graph, a, b), (visited + [node], []), graph[node][2])

# you should have this one
def findtrees(graph):
    return foldr(lambda a,b: helper(graph, a, b), ([], []), list(range(len(graph))))[1]
        
print(findtrees(g))

