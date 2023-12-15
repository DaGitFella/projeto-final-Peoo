import tkinter as tk
from turtle import back, width

window = tk.Tk()
window.geometry("350x450")
window.configure(background="black")
window.title("listagem")

frame1 = tk.Frame(background="white")
frame1.pack(pady=50)

frame2 = tk.Frame()
frame2.pack()

insert = {
    "inserir":tk.Label(frame1, text='inserir número', background="white"),
    "label":tk.Label(frame1, width=250, background="black"),
    "button":tk.Button(frame2, text="inserir", command=lambda: print('botão')),
}

for widget in insert.values():
    widget.pack()

window.resizable(False, False)
window.mainloop()