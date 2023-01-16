def solution(number): 
    cnt = 0
    length=len(number)
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                print(number[i],",",number[j],",",number[k],)
                if number[i]+number[j]+number[k]==0:
                    cnt +=1
    return cnt