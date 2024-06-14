import tkinter as tk

win = tk.Tk()
win.title('회원가입')
win.geometry('300x200')

def submit():
    name = ent1.get()
    grade = rv.get()
    hobbies = []
    if cv1.get():
        hobbies.append("영화시청")
    if cv2.get():
        hobbies.append("음악감상")
    if cv3.get():
        hobbies.append("사진찍기")
    if cv4.get():
        hobbies.append("운동")
    print(f"이름: {name}")
    print(f"학년: {grade}")
    print(f"취미: {', '.join(hobbies)}")
    

def close():
    win.distroy

lab1 = tk.Label(win)
lab1.config(text = '이름:')
lab1.pack()

ent1 = tk.Entry(win)
ent1.pack()


lab2 = tk.Label(win)
lab2.config(text = '학년:')
lab2.pack()

rv = tk.StringVar(value = '1학년')
rb1 = tk.Radiobutton(win, text = '1학년',value = '1학년',variable = rv)
rb2 = tk.Radiobutton(win, text = '2학년',value = '2학년',variable = rv)
rb3 = tk.Radiobutton(win, text = '3학년',value = '3학년',variable = rv)
rb4 = tk.Radiobutton(win, text = '4학년',value = '4학년',variable = rv)
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

lab3 = tk.Label(win)
lab3.config(text = '취미:')
lab3.pack()

cv1 = tk.BooleanVar()
cb1 = tk.Checkbutton(win, text = '영화시청',variable = cv1)
cv2 = tk.BooleanVar()
cb2 = tk.Checkbutton(win, text = '음악감상',variable = cv2)
cv3 = tk.BooleanVar()
cb3 = tk.Checkbutton(win, text = '사진찍기',variable = cv3)
cv4 = tk.BooleanVar()
cb4 = tk.Checkbutton(win, text = '운동',variable = cv4)
cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()

btn1 = tk.Button(win)
btn1.config(text = '입력')
btn1.config(command = submit)
btn1.pack()

btn2 = tk.Button(win)
btn2.config(text = '종료')
btn2.config(command = close)
btn2.pack()

win.mainloop()
