def solution(phone_number):
    phone_len = len(phone_number)
    phone_number = phone_number[-4:]
    phone_number = "*"*(phone_len-4)+phone_number
    return phone_number