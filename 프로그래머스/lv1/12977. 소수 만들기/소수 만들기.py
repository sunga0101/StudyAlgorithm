from itertools import combinations
def solution(nums):
    answer = []
    cnt=0
    for i,j,k in (combinations(nums,3)):
        answer.append((i+j+k))
    
    for i in answer:
        ch=0
        for j in range(2,i):
            if i%j==0:
                ch=1
        if ch==0:
            cnt+=1
     
    return cnt