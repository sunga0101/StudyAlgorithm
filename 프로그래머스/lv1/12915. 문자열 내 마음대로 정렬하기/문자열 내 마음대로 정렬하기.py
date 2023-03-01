def solution(strings, n):
    strings=sorted(strings)
    a=dict()
    for i in strings:
        alpha=i[n]
        a[i]=ord(alpha)
    list=sorted(a.items(),key=lambda x:x[1])
    answer = [ x[0] for x in list  ]
    return answer