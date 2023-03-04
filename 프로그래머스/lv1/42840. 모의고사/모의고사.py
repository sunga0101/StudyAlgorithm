def solution(answers):
    score = [0]*4
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    for i in range(len(answers)):
        if answers[i]==a[i%5]:
            score[1] +=1
        if answers[i]==b[i%8]:
            score[2] +=1
        if answers[i]==c[i%10]:
            score[3] +=1
            
    for i in range(len(score)):
        if max(score)== score[i]:
            answer.append(i)
        
    return answer