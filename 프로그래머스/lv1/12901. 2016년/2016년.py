def solution(a, b):
    answer = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days=0
    month = [0]*13
    for i in range(1, 13):
        if i == 2:
            month[i]=29
        elif i in (1,3,5,7,8,10,12):
            month[i]=31
        else:
            month[i]=30
            
    for j in range(1,a):
        days+=month[j]
    days+=b
    print(month)
    return(answer[days%7])