def solution(s): #길이 확인, 숫자로만 구성 
    if len(s) == 4 or len(s)==6:
        for i in s:
            if i.isalpha():
                break
        else:
            return True 
    return False