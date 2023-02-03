def solution(array, commands):
    answer = []
    for i,j,k in commands:
        print(i,j,k)
        new = sorted(array[i-1:j])
        answer.append(new[k-1])
    return answer