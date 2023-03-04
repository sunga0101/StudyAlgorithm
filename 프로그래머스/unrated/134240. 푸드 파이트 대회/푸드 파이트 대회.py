def solution(food):
    answer = ''
    stack =[]
    for i in range(1, len(food)):
        if food[i] != 1:
            a = food[i]//2 
            answer=answer+str(i)*a
            stack.append(str(i)*a)
    answer+='0'
    while stack:
        answer+=stack.pop()
    return answer