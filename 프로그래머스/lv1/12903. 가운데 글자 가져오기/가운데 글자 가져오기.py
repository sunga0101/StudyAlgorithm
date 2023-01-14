def solution(s): 
    length=len(s)
    i= round((length/2)+0.00001)-1 
    if length%2==0:
        return s[i:i+2]
    else:    
        return s[i]