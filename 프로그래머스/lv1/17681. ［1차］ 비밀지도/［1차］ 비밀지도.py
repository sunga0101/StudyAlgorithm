a=''
def solution(n, arr1, arr2):
    global a
    result=[]
    answer1 = []
    answer2 = []
    
    for i in arr1:
        a=''
        c=DFS(i)
        if len(c) != n:
            c='0'*(n-len(c))+c
        answer1.append(c)
    print(answer1)
    
    for i in arr2:
        a=''
        c=DFS(i)
        if len(c) != n:
            c='0'*(n-len(c))+c
        answer2.append(c)
    
    for k in range(n):
        s=''
        for j in range(n):
            if answer1[k][j]==answer2[k][j] and answer1[k][j]=='0':
                s+=" "
            else:
                s+='#'
        print(s)
        result.append(s)
    return result


def DFS(v):
    global a
    if v!=0:
        DFS(v//2)
        a+=str(v%2)
    return a