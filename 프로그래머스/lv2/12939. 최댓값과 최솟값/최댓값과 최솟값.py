import heapq as hq
def solution(s):
    slist = list(map(str, s.split()))
    print(slist)
    a=[]
    b=[]
    for i in slist:
        i=int(i)
        hq.heappush(a,i)
        hq.heappush(b,-i)
    res_a=hq.heappop(a)
    res_b=hq.heappop(b)
    res=str(res_a)+" "+str(-res_b)
    return res