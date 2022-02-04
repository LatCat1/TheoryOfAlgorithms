
# some code to run dijkstra's algo for pset 2
def d():
    edges = {
        'a': {
            'b': 4,
            'd':4,
            'e':3
        },
        'b': {
            'c':2,
            't':6,
            'f':7
        },
        'c':{
            't':12,
            'a':1
        },
        'd': {
            'c': 6
        }, 
        'e': {
            'd': 10,
            'g': 6
        },
        'f': {
            'j':4,
            't':2
        },
        'g': {
            'd': 4,
            'h': 5
        },
        'h': {
            'f':22,
            't':25
        },
        'i':{
            'g':1,
            'h':2
        },
        'j': {
            'h':2,
            'i':3,
            'b':20
        },
        's': {
            'i':10,
            'e':4,
            'a':21,
            'g':11,
            'j':5
        },
        't': {

        }
    }

    costs = {'s':0}
    queue = []
    for e in edges['s']:
        queue.append((edges['s'][e], 's' + e))
    queue.sort()

    while 't' not in costs:
        cost, edge = queue.pop(0)
        f = edge[0]
        t = edge[1]
        # print(f'Considering edge ${edge}$; ', end='')
        if t in costs:
            # print('it is discarded.\\\\')
            pass
        else:
            costs[t] = cost
            # print(f'it is taken, so the distance from $s$ to ${t}$ is {cost}.\\\\')
            for t2 in edges[t]:
                queue.append((costs[t]+edges[t][t2], t+t2))
        queue.sort()


def four_sum(nums, target):
    pairsums = [] # ends at length n^2
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pairsums.append((nums[i] + nums[j], (i,j)))
    pairsums.sort() # takes O(n^2logn^2)=O(n^2logn)

    for i in range(len(pairsums)):
        # this check is lazy and slow, but is O(log n^2) when done with a binary tree
        current, pair = pairsums[i]
        for a,b in pairsums[i+1:]:
            if current + a == target and pair[0] != b[0] and pair[1] != b[0] and pair[1] != b[0] and pair[1] != b[1]:
                return (nums[pair[0]], nums[pair[1]], nums[b[1]], nums[b[0]])
    return None


if __name__ == '__main__':
    print(four_sum([1,2,3,-4,5,6,7], 10))