def solution(s):
    alpha = [0]*27
    result = []
    for x, y in enumerate(s):
        x=x+1
        idx=ord(y)-96 #a가 alpha[1]번에 오도록
        if alpha[idx]==0: 
            alpha[idx]= x
            result.append(-1)
        else:
            result.append(x-alpha[idx])
            alpha[idx]=x
    return result