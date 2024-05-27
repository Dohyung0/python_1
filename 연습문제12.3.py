import os

# 장바구니 리스트 초기화
shopping_bag = []

# 파일에서 장바구니 읽기
def load_shopping_bag(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                item = line.strip()
                if item:  # 빈 줄을 무시
                    shopping_bag.append(item)

# 장바구니 파일에 저장하기
def save_shopping_bag(filename):
    with open(filename, 'w', encoding='utf8') as file:
        for item in shopping_bag:
            file.write(f"{item}\n")

# 장바구니 보기
def show_shopping_bag():
    print(f">>> 장바구니 보기: {shopping_bag}")

# 메인 프로그램
def main():
    filename = 'shoppingbag.txt'
    load_shopping_bag(filename)

    while True:
        print("[구입]")
        item = input("상품명? ")
        if item:
            shopping_bag.append(item)
            print(f"장바구니에 {item}가(이) 담겼습니다.")
        else:
            break
    
    show_shopping_bag()
    save_shopping_bag(filename)
if __name__ == "__main__":
    main()
