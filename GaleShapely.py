
A = [
    [1,2,3,0],
    [1,2,0,3],
    [2,1,0,3],
    [0,3,1,2]
]

B = [
    [2,1,3,0],
    [3,2,0,1],
    [3,0,2,1],
    [2,0,1,3]
]

def galeShapely(A, B, debug=False, A_name='A', B_name='B'):
    pairs = [None]*len(A) # list, indexed bo woman, of who her pair is
    while None in pairs: #while there is some unpaired woman
        proposals = [[] for _ in range(len(B))] #a list, indexed by woman, of who proposed to her
        for i in range(len(A)): #loop through each man
            if i not in pairs: #if they aren't paired with a woman
                if debug:
                    print(f'{A_name}{i+1} proposes to {B_name}{A[i][0]+1}')
                proposals[A[i].pop(0)].append(i) #they propose to her
        # print(proposals)
        # so all women now have their proposals
        for i in range(len(B)): #loop through each woman
            for j in proposals[i]: #loop through each man who proposed to her
                if pairs[i] is None or B[i].index(j) < B[i].index(pairs[i]):
                    if debug:
                        print(f'{B_name}{i+1} accepts {A_name}{j+1}\'s proposal')
                    pairs[i] = j
                else:
                    if debug:
                        print(f'{B_name}{i+1} rejects {A_name}{j+1}\'s proposal')
        if debug:
            for i in range(len(A)):
                if i not in pairs:
                    print(f'{A_name}{i+1} is not engaged; ', end='')
                else:
                    print(f'{A_name}{i+1} is engaged to {B_name}{pairs.index(i)+1}; ', end='')
            print()
        # print(pairs)
    q = [None]
    for p in pairs: q.append(p+1)
    return q

print(galeShapely(B, A, True, A_name='B', B_name='A'))