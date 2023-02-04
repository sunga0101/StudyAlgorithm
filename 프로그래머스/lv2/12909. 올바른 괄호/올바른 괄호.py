def solution(s):
    if len(s)==1 or len(s) %2 !=0  : #괄호가 하나거나 홀수개
        return False
    if s[0]=='(' and s[-1]==')':
        left_cnt=0
        right_cnt=0
        for i in s:
            if i=='(':
                left_cnt +=1
            elif i ==')':
                right_cnt +=1
            if left_cnt <right_cnt:
                return False
        if left_cnt != right_cnt:
            return False
        else:
            return True
    
    return False