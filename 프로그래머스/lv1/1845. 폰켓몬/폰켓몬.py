def solution(nums):
    half = len(nums)//2
    num=set(nums)
    answer=len(num)
    if answer > half:
        answer=half
    return answer