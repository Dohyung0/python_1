def leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False
def month_days(y,m):
    if m == 2:
        if leap_year(y):
            return '29'
        else:
            return '28'
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return '30'
    else:
        return '31'
        
y = int(input('연도?'))
m = int(input('월?'))
while m < 1 or m > 12:
    m = int(input('월을 다시 입력하세요:'))
d = month_days(y,m)
print(f'{y}년 {m}월은 {d}일까지 있습니다.')

