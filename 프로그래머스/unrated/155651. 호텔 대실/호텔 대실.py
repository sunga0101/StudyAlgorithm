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

'''
[['14:10', '19:20'], ['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['18:20', '21:20']]

['14:10', '19:20'] 19:30
['14:20', '15:20'] 15:30 ['16:40', '18:20']
['15:00', '17:00'] 17:10 ['18:20', '21:20']


1. 소팅하기
2. 첫번째 껀 일단 무조건 넣고  cnt +1
가능한시간리스트 = [첫번째 끝나는 시간 + 10]
3. 두번째 꺼 받아서 > 첫번째끝나는시간+10 이면
cnt+1, 가능한시간리스트 = [첫번째 끝나는 시간 + 10, 두번째끝나는시간 +10]
4. 세번째 꺼 받아서 가능한시간리스트에 보다 작으면? 넣고 그 시간을 업뎃 
5. 마지막으로 시간리스트의 개수
'''