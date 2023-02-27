def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():#대문자
            ch=(ord(i)+n) 
            if ch>90:
                ch %=90
                answer+=chr(ord('A')+ch-1)
            else:
                answer+=chr(ch)
        elif i.islower():#소문자
            ch=(ord(i)+n) 
            if ch>122:
                ch %= 122
                answer+=(chr(ord('a')+ch-1))
            else:
                answer+=(chr(ch))
        else:
            if i==' ':
                answer+=(" ")
    return answer