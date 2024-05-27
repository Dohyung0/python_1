from datetime import datetime
import os

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

def get_current_time():
    now = datetime.now()
    return Time(now.hour, now.minute)

def save_time(time):
    with open('last.dat', 'w', encoding='utf8') as file:
        file.write(f"{time.hour}\n{time.minute}")

def load_time():
    try:
        with open('last.dat', 'r', encoding='utf8') as file:
            hour = int(file.readline().strip())
            minute = int(file.readline().strip())
            return Time(hour, minute)
    except FileNotFoundError:
        return None

def main():
    print("현재 작업 디렉토리:", os.getcwd())  # 현재 작업 디렉토리 출력
    
    last_time = load_time()
    current_time = get_current_time()
    
    if last_time is None:
        print("안녕하세요, 처음 실행되었습니다.")
    else:
        print(f"안녕하세요, 마지막으로 {last_time}에 실행되었습니다.")
    
    print(f"지금은 {current_time} 입니다.")
    
    save_time(current_time)

if __name__ == "__main__":
    main()
