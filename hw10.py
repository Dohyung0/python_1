import pickle
import os

filename = 'scores.bin'

scores = []
def input_scores():
    i = 1
    print('[점수 입력]')
    while True:
        num = int(input(f'#{i}? '))
        if num == -1:
            break
        scores.append(num)
        i += 1
def get_average():
    n = len(scores)
    s = 0
    for i in range(n):
        scores[i]
        s += scores[i]
    avg = s/n
    return avg
def show_scores():
    print('\n[점수 출력]')
    n = len(scores)
    print('개인점수:', end=' ')
    for i in range(n):
        print(scores[i], end=' ')
    avg = get_average()
    print('\n평균:',end=' ')
    print(f'{avg:.1f}')

def save_scores(filename):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename):
    with open(filename, 'rb') as f:
        scores = pickle.load(f)
    return scores

scores = input_scores()
show_scores(scores)
save_scores(scores)
loaded_scores = load_scores()
show_scores(loaded_scores)

