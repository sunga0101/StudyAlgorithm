def solution(numbers):
    s = set()
    for i in range(len(numbers)-1): #0~n-1
        for j in range(i+1,len(numbers)):
            
            sum = numbers[i]+numbers[j]
            s.add(sum)
            print(sum,numbers[i],numbers[j])
    s=list(s)
    return sorted(s)