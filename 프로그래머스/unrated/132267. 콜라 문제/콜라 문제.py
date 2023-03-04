def solution(a, b, n):
    mybottle = n
    given=[]
    while mybottle//a >0:
        if mybottle%a ==0 : 
            mybottle = mybottle//a*b 
            given.append(mybottle) 
            print(mybottle,1)
        else:
            given.append(mybottle//a*b)
            mybottle=mybottle%a+mybottle//a*b 
            print(mybottle,2)
    print(given)
    return sum(given)
