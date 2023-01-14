def solution(s): #z>a>Z>A abdAF -> dbaFA
    arr = list(s)
    str_alpha = ''.join(sorted(arr, reverse=True))
    return str_alpha