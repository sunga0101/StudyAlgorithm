def solution(absolutes, signs):
    res=0
    for i in range(len(absolutes)):
        if signs[i]:
            res+=absolutes[i]
        else:
            res+=(absolutes[i]*-1)
    return res