# case
# "2022.02.28"   ["A 23"]   ["2020.01.28 A"]   [1]
def solution(today, terms, privacies):
    deadline = [0]*26
    res = []
    today_yyyy, today_mm, today_dd = date(today)
    for i in terms:
        alpha, month=(map(str, i.split()))
        idx=ord(alpha)-ord('A')
        deadline[idx]=month
    for j in range(len(privacies)):
        started, linked_alpha = (map(str, privacies[j].split()))
        linked_idx=ord(linked_alpha)-ord('A')
        start_yyyy, start_mm, start_dd = date(started)
        start_mm += int(deadline[linked_idx])  #"2020.24.28"   
        if start_dd != 1:
            start_dd -= 1  #"2020.24.27"   
        else: #1일일때
            start_dd = 28
            if start_mm >1:
                start_mm -= 1
            elif start_mm == 1:
                start_mm = 12
                start_yyyy-=1
                
        if start_mm >12: #"2020.24.27"  
            start_yyyy += (start_mm//12)   #"2022.24.27"  
            start_mm -= (start_mm//12)*12   #"2022.0.27"  
        if start_mm == 0:
            start_mm =12  #"2022.12.27"  
            start_yyyy -= 1 #"2021.12.27"  
            
        
        print("!!",start_yyyy,start_mm,start_dd)
        if today_yyyy > start_yyyy:
            res.append(j+1)
        elif today_yyyy < start_yyyy:
            continue
        else: #같을때
            if today_mm > start_mm:
                res.append(j+1)
            elif today_mm < start_mm:
                continue
            else: # 년 월 모두 같으면
                if today_dd > start_dd:
                    res.append(j+1)
                elif today_dd <= start_dd:
                    continue
        # print("!!",start_yyyy,start_mm,start_dd)
    return res

def date(str_date):
    yyyy=str_date[:4]
    mm=str_date[5:7]
    dd=str_date[8:]
    return(int(yyyy),int(mm),int(dd))






