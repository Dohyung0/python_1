def electric_summer(amount):
    if amount < 0:
        return '오류'
    elif amount <= 300:
        return 910 + 120 * amount
    elif amount <= 450:
        return 910 + 120 * 300 + 1600 + 214.6 * (amount - 300)
    else:
        return 910 + 120 * 300 + 1600 + 214.6 * 150 + 7300 + 307.3 * (amount - 450)

def electric(amount):
    if amount < 0:
        return '오류'
    elif amount <= 200:
        return 910 + 120 * amount
    elif amount <= 400:
        return 910 + 120 * 200 + 1600 + 214.6 * (amount - 200)
    else:
        return 910 + 120 * 200 + 1600 + 214.6 * 200 + 7300 + 307.3 * (amount - 400)
     
def month_electric(month, elec):
    if month == 7 or month == 8:
        a = electric_summer(elec)
        return a
    else:
        b = electric(elec)
        return b

# 사용자 입력
month = int(input('몇월인가요?'))
while month > 12 or month < 1:
        month = int(input('몇월인가요?'))
elec = float(input('몇kwh 사용하셨나요?'))

# 함수 호출 및 결과 출력
a = month_electric(month, elec)
print(f'{a}원 지불하셔야 합니다.')

        
        

    

        
        
    
     
    


        
    
    
