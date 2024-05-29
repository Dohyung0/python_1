import pickle
import os

def input_scores():
    scores = []
    i = 1
    print('[점수 입력]')
    while True:
        num = int(input(f'#{i}? '))
        if num == -1:
            break
        scores.append(num)
        i += 1
    return scores

def get_average(scores):
    n = len(scores)
    s = sum(scores)
    avg = s / n
    return avg

def show_scores(scores):
    print('\n[점수 출력]')
    print('개인점수:', end=' ')
    for score in scores:
        print(score, end=' ')
    avg = get_average(scores)
    print('\n평균:', end=' ')
    print(f'{avg:.1f}')

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)
    print(f'점수가 {filename}에 저장되었습니다.')

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            scores = pickle.load(f)
        print('[파일 읽기]')
        return scores

filename = 'score.bin'
scores = load_scores(filename)

if scores:
    show_scores(scores)
else:
    scores = input_scores()
    show_scores(scores)
    save_scores(scores)

