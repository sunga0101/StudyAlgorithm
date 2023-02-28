from collections import deque
def solution(t, p):
    cnt=0
    n=len(p)
    k=len(t)-n+1
    for i in range(k):
        str=t[:n]
        t=t[1:]
        if str <= p:
            cnt+=1
    return cnt