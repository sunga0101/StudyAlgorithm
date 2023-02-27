from collections import deque

def solution(elements):
    n = len(elements)
    dq = deque(elements)
    res = set()
    for _ in range(n):
        s=0
        for j in range(n):
            s += (dq[j])
            res.add(s)
        cur=dq.popleft()
        dq.append(cur)
    return len(res)