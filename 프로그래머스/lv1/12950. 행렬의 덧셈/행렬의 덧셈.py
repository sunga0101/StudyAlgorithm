def solution(arr1, arr2):
    new_arr = arr1
    for i in range(len(arr1)):
        # print(arr1[i])
        for j in range(len(arr1[i])):
            new_arr[i][j] =arr1[i][j]+arr2[i][j]
    return new_arr