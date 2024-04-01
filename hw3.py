def get_fixed_price(discount_rate, discounted_price):
    fixed_price = discounted_price / (100 - discount_rate) * 100
    return fixed_price


discount_rate = int(input("할인율은?"))
A_discounted_price = int(input("A 상품의 할인된 가격은?"))
B_discounted_price = int(input("B 상품의 할인된 가격은?"))
A_fixed_price = get_fixed_price(discount_rate, A_discounted_price)
B_fixed_price = get_fixed_price(discount_rate, B_discounted_price)
print("A 상품의 정가는",A_fixed_price,"원")
print("B 상품의 정가는",B_fixed_price,"원")



