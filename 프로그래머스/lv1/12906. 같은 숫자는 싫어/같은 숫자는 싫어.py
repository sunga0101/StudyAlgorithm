from collections import deque

def solution(arr):
    res=[]
    dq=deque(arr)
    while dq: 
        a= dq.popleft()
        if ( a in res):
            if res[-1] != a:
                res.append(a)
        else:
            res.append(a)
    return res