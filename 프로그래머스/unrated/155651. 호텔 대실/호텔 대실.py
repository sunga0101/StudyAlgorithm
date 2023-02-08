import re
def solution(book_time):
    book_time.sort()
    change = []
    fin_time=[]
    
    for i in range(len(book_time)):
        # print(book_time[i]) 
        # a= book_time[i] # a = ['12:00', '12:00']
        s=''
        for j in book_time[i]: # j -> 12:00
            s+= re.sub(r"[^0-9]", "", j)
        change.append(int(s))
        # print(s)
    # print("change1 :", change)
        
    for i in range(len(change)):
        
        started=change[i]//10000
        finished=change[i]-started*10000+10
        # print("!! :", finished%100)
        # print("!! :", finished+40)

        if finished%100 >= 60: # 1761, 1860
            finished=finished+40
            
        # print("started:",started, "finished:", finished)
        # 첫번째는 그냥 넣기
        if change[i] ==change[0]:
            fin_time.append(finished)
        #두번째부터 비교
        else:
            for j in range(len(fin_time)):
                if started >= fin_time[j]:
                    fin_time[j]=finished
                    break
                elif j==(len(fin_time)-1):
                    fin_time.append(finished)
        # print("현재상황:",fin_time) 
                
        
        
    # print("change2 :", change)
    # print("fin_time :", fin_time)
    return len(fin_time)
