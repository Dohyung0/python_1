import tkinter as tk

def submit():
    name = ent_name.get()
    grade = var_grade.get()
    hobbies = []
    if var_movie.get():
        hobbies.append("영화시청")
    if var_music.get():
        hobbies.append("음악감상")
    if var_photo.get():
        hobbies.append("사진찍기")
    if var_sport.get():
        hobbies.append("운동")
    print(f"이름: {name}")
    print(f"학년: {grade}")
    print(f"취미: {', '.join(hobbies)}")

def close_app():
    win.destroy()

win = tk.Tk()
win.title('회원가입')
win.geometry('300x200')

# 이름 입력
lab_name = tk.Label(win, text='이름:')
lab_name.grid(row=0, column=0, padx=10, pady=5)

ent_name = tk.Entry(win)
ent_name.grid(row=0, column=1, padx=10, pady=5)

# 학년 선택
lab_grade = tk.Label(win, text='학년:')
lab_grade.grid(row=1, column=0, padx=10, pady=5)

var_grade = tk.StringVar(value="1학년")
rbtn_grade1 = tk.Radiobutton(win, text='1학년', variable=var_grade, value='1학년')
rbtn_grade1.grid(row=1, column=1, sticky='w')

rbtn_grade2 = tk.Radiobutton(win, text='2학년', variable=var_grade, value='2학년')
rbtn_grade2.grid(row=1, column=2, sticky='w')

rbtn_grade3 = tk.Radiobutton(win, text='3학년', variable=var_grade, value='3학년')
rbtn_grade3.grid(row=1, column=3, sticky='w')

rbtn_grade4 = tk.Radiobutton(win, text='4학년', variable=var_grade, value='4학년')
rbtn_grade4.grid(row=1, column=4, sticky='w')

# 취미 선택
lab_hobby = tk.Label(win, text='취미:')
lab_hobby.grid(row=2, column=0, padx=10, pady=5)

var_movie = tk.BooleanVar()
chk_movie = tk.Checkbutton(win, text='영화시청', variable=var_movie)
chk_movie.grid(row=2, column=1, sticky='w')

var_music = tk.BooleanVar()
chk_music = tk.Checkbutton(win, text='음악감상', variable=var_music)
chk_music.grid(row=2, column=2, sticky='w')

var_photo = tk.BooleanVar()
chk_photo = tk.Checkbutton(win, text='사진찍기', variable=var_photo)
chk_photo.grid(row=2, column=3, sticky='w')

var_sport = tk.BooleanVar()
chk_sport = tk.Checkbutton(win, text='운동', variable=var_sport)
chk_sport.grid(row=2, column=4, sticky='w')

# 버튼
btn_submit = tk.Button(win, text='입력', command=submit)
btn_submit.grid(row=3, column=0, columnspan=5, pady=10)

btn_exit = tk.Button(win, text='종료', command=close_app)
btn_exit.grid(row=4, column=0, columnspan=5, pady=5)

win.mainloop()
