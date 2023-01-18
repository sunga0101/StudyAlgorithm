def solution(n, m): # 최대공약수 최소공배수 
    answer = []
    max_num = 0
    min_num = max(n,m)
    for i in range(1,(min(n,m)+1)):
        if n%i==0 and m%i==0:
            max_num=i
            
    while min_num <=n*m:
        if min_num%n!=0 or min_num%m!=0:
            min_num+=1
        elif min_num%n==0 or min_num%m==0:
            break;
            
    return max_num, min_num