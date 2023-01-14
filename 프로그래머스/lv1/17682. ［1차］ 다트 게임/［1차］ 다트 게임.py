import re
#점수/보너스/(옵션) -> 점수 0~10 / SDT / [*,#]-> 존재 할수도 안할수도
#* -> 이번 기회 *2, 이전 기회 *2 /  *, #와 중첩가능
## -> 이번 기회 마이너스, 이전 기회 *2
# (1*1 )*2+ (2*2) *2 + 3*3*3
def solution(dartResult): 
    sum=0
    chance=0 #기회
    res_arr=[] #[first, second,third]
    #1일때는 뒤에 0인지 확인
    res_arr = re.findall(r'\d+', dartResult) # r'\d+'
    for r in range(len(res_arr)):
        res_arr[r]=int(res_arr[r])
        
    for i in range(len(dartResult)): 
        #3번의 기회 -> 숫자나오면 res 순서로 넣기
        a= (ord(dartResult[i])-48)
        if a>=0 and a<=9:
            continue
        else:
            if dartResult[i]=='S':
                chance+=1
                res_arr[chance-1]= res_arr[chance-1]*1
            elif dartResult[i]=='D':
                chance+=1
                res_arr[chance-1]= res_arr[chance-1]*res_arr[chance-1]
            elif dartResult[i]=='T':
                chance+=1
                res_arr[chance-1]=res_arr[chance-1]*res_arr[chance-1]*res_arr[chance-1]
            elif dartResult[i]=='*':
                if chance>=2:
                    res_arr[chance-2]=res_arr[chance-2]*2 #앞점수
                res_arr[chance-1]=res_arr[chance-1]*2
            elif dartResult[i]=='#':
                res_arr[chance-1] *= -1
    #합구하기
    for r in (res_arr):
        sum +=r

    return sum