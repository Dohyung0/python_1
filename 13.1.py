import tkinter as tk

win = tk.Tk()
win.geometry('1000x500')
win.title('온도변환기')

lab1 = tk.Label(win)
lab1.config(text = '화씨')

ent1 = tk.Entry(win)
ent1.pack()
def ftoc():
    F = float(ent1.get())
    C = (F - 32) * 5/9
    ent2.delete(0,tk.END)
    ent2.insert(0,f'{C:.2f}')

btn1 = tk.Button(win)
btn1.config(text = '화씨->섭씨')
btn1.config(command = ftoc)
btn1.pack()

lab2 = tk.Label(win)
lab2.config(text = '섭씨')

ent2 = tk.Entry(win)
ent2.pack()
def ctof():
    C = float(ent2.get())
    F = (C * 9/5) + 32
    ent1.delete(0,tk.END)
    ent1.insert(0,f'{F:.2f}')
    
btn2 = tk.Button(win)
btn2.config(text = '섭씨->화씨')
btn2.config(command = ctof)
btn2.pack()

def delete():
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    
btn3 = tk.Button(win)
btn3.config(text = '초기화')
btn3.config(command = delete)
btn3.pack()

def close():
    win.destroy()
    
btn4 = tk.Button(win)
btn4.config(text = '종료')
btn4.config(command = close)
btn4.pack()

win.mainloop()
