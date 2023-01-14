def solution(left, right):
    answer = 0
    value = 0
    cnt = 0
    for i in range(left, right+1): #13~17
        cnt = 0
        for j in range(1, i+1): #1~13
            if i%j==0: #약수인 경우
                cnt += 1
        if cnt %2==0: #even:
            value += i
        elif cnt %2 != 0:
            value -= i
    return value