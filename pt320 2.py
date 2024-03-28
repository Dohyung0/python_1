def get_radius(prompt):
    r = int(input(prompt))
    x = r*r*3.14
    return x

input_r = int(input("넓이를 구하고자 하는 원의 반지름은?"))
result = get_radius(input_r)
print(result)
