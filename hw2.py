#사용자 정의 함수부
def exchange(amount):
    n500 = amount//500
    x = amount%500
    n100 = x//100
    x%= 100
    n50 = x//50
    x%= 50
    n10 = x//10
    print("500원 동전의 개수:" ,n500,)
    print("100원 동전의 개수:" ,n100,)
    print("50원 동전의 개수:" ,n50,)
    print("10원 동전의 개수:" ,n10,)
    
    

def get_integer(prompt):
    res = int(input(prompt))
    return res 
    



#주 프로그램부
exchange_amount = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(exchange_amount)
    
