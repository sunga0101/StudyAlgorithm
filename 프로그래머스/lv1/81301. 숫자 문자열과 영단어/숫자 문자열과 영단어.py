from collections import deque
def solution(s):
    s=deque(list(s))
    answer = ''
    while len(s)!=0: #리스트가 비면 stop
        x=s.popleft()    
        if x.isdecimal():
            answer+=x
        elif x.islower():
            if x=='o'and len(s)>=1:
                s.popleft()
                s.popleft()
                answer+='1'
            
            elif x=='z'and len(s)>=2:
                s.popleft()
                s.popleft()
                s.popleft()
                answer+='0'
            
            elif x=='e' and len(s)>=3:
                s.popleft()
                s.popleft()
                s.popleft()
                s.popleft()
                answer+='8'
                
            elif x=='n'and len(s)>=2:
                s.popleft()
                s.popleft()
                s.popleft()
                answer+='9'
                
            elif x=='t':
                y=s.popleft()
                if y=='w'and len(s)>=0:  
                    s.popleft()
                    answer+='2'
                elif y=='h'and len(s)>=2:  
                    s.popleft()
                    s.popleft()
                    s.popleft()
                    answer+='3'
                    
            elif x=='f':
                y=s.popleft()
                if y=='o'and len(s)>=1:  
                    s.popleft()
                    s.popleft()
                    answer+='4'
                elif y=='i'and len(s)>=1: 
                    s.popleft()
                    s.popleft()
                    answer+='5'
                    
            elif x=='s':
                y=s.popleft()
                if y=='i'and len(s)>=0:  
                    s.popleft()
                    answer+='6'
                elif y=='e'and len(s)>=2: 
                    s.popleft()
                    s.popleft()
                    s.popleft()
                    answer+='7'
        
    
    return int(answer)