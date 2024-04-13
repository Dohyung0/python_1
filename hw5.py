def read_single_digit(integer):
    if integer == 0:
        return '공'
    if integer == 1:
        return '일'
    if integer == 2:
        return '이'
    if integer == 3:
        return '삼'
    if integer == 4:
        return '사'
    if integer == 5:
        return '오'
    if integer == 6:
        return '육'
    if integer == 7:
        return '칠'
    if integer == 8:
        return '팔'
    if integer == 9:
        return '구'
    else:
        return '오류'

def read_number(num):
    first = int(num[0])
    second = int(num[1])
    third = int(num[2])
    first_num = read_single_digit(first)
    second_num = read_single_digit(second)
    third_num = read_single_digit(third)
    return f'{first_num} {second_num} {third_num}'

num = input('정수를 입력하세요:')
print(read_number(num))

