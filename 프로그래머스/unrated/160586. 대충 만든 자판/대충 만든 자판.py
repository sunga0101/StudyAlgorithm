def solution(keymap, targets):
    alpha = [101]*26
    answer = []
    print(keymap)
    for i in range(len(keymap)):
        print(keymap[i])
        for index, j in enumerate(keymap[i]):
            if alpha[ord(j)-ord('A')] > index+1:
                alpha[ord(j)-ord('A')]=index+1
    print(alpha)
    for k in range(len(targets)):
        sum=0
        for h in targets[k]:
            seq = ord(h)-ord('A')
            if alpha[seq] != 101:
                sum += alpha[seq]
            else:
                sum = -1
                break
        print(sum)
        answer.append(sum)
    return answer