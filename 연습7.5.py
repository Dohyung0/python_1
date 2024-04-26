def find_char_type(char):
    if '0'<=char<='9':
        return '숫자 문자'
    elif 'a'<=char<= 'z':
        return '알파벳 문자'
    elif 'A'<=char<='Z':
        return '알파벳 문자'
    elif ' ':
        return '공백 문자'
    else:
        return '기타 문자'

char = input('한 문자 입력?')
typ = find_char_type(char)
print(f'{typ}를 입력했습니다.')

