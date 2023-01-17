def solution(sizes):
    answer = 0
    max_first = -1
    max_second = -1
    for i in range(len(sizes)):
        print(i)
        if (sizes[i][0] < sizes[i][1]):
            tmp = sizes[i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=tmp
        if max_first < sizes[i][0]:
            max_first = sizes[i][0]
        if max_second < sizes[i][1]:
            max_second = sizes[i][1]
    return max_first*max_second