def solution(n):
    m = n # m은 몫
    extra = 0 # 나머지
    res=0
    cnt = 0
    result = 0
    while m > 0:
        extra = m%3
        m = m//3
        res = res*10 + extra
        
    while res>0:
        extra = res%10
        res= res//10
        result += extra * pow(3,cnt)        
        cnt += 1

    return result