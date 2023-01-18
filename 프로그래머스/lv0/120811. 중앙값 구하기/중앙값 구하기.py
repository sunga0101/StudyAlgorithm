def solution(array):
    array.sort()
    return (array[round((len(array)/2)+0.5)-1])