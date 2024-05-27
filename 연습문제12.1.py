import os
content = """안녕하세요, 반갑습니다.
이 파일은 테스트 파일 저작을 위해 작성된 텍스트 문서입니다.
조금 낯설더라도 포기하지 마세요
"""

with open('readme.txt', 'w', encoding='utf8') as file:
    file.write(content)
current_directory = os.getcwd()
print("현재 작업 디렉토리:", current_directory)

def show_file(filename):
    with open(filename, 'r', encoding = 'utf8') as file:
        i = 1
        while True:
            line = file.readline() # 한 줄을 읽어 반환
            if line == '':
                break
            print(f'{i}: {line.strip()}')
            i += 1

# 주 프로그램부
fn = input('파일명: ')
show_file(fn)
