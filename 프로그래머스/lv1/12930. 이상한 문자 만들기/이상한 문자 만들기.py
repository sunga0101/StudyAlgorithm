def solution(s):
    s=list(s)
    answer = ''
    wordIdx = 0
    
    for k in range(len(s)):
        if s[k] ==' ':
            wordIdx = 0
        else:
            if wordIdx %2==0:
                t=s[k]
                s[k]=t.upper()
                wordIdx+=1
            else:
                t=s[k]
                s[k]=t.lower()
                wordIdx+=1
        answer+=s[k]
    return answer