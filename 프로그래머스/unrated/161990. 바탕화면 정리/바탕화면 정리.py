def solution(wallpaper):
    left=[]
    right=[]
    for i_idx, i in enumerate(wallpaper):
        if '#' in i:
            left.append(i_idx)
        for j_idx, j in enumerate(i):
            if j != ".":
                right.append(j_idx)
    return (min(left),min(right),max(left)+1, max(right)+1)